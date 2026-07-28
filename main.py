from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import (
    http_exception_handler as og_http_exception_handler,
    request_validation_exception_handler as og_request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from errors import UnicornError
from routers import routers

app = FastAPI()


for router in routers:
    app.include_router(router)


@app.get("/")
def read_root():  # noqa
    return {"Title": "Welcome to danilober's FastAPI tutorial notes!"}


@app.exception_handler(UnicornError)
async def unicorn_exception_handler(request: Request, exc: UnicornError):  # noqa
    return JSONResponse(
        status_code=418, content={"message": f"Oops! {exc.name} did something..."}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):  # noqa
    message = "Validation errors:"
    for error in exc.errors():
        message += f"\nField: {error['loc']}. Error: {error['msg']}"
    return PlainTextResponse(message, status_code=400)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):  # noqa
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def override_validation_with_body_handler(  # noqa
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=418,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.exception_handler(StarletteHTTPException)
async def custom_reuse_http_exc_handler(request: Request, exc: StarletteHTTPException):  # noqa
    print(f"Reusing HTTP exception handler: {repr(exc)}")  # noqa: RUF010
    return await og_http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def custom_reuse_validation_exc_handler(  # noqa
    request: Request, exc: RequestValidationError
):
    print(f"Reusing request validation exception handler: {exc}")
    return await og_request_validation_exception_handler(request, exc)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
