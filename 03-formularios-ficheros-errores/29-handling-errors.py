"""29/111 - Handling Errors
https://fastapi.tiangolo.com/tutorial/handling-errors/
"""

from typing import Annotated

from fastapi import APIRouter, Body, FastAPI, HTTPException

from errors import UnicornError

app = FastAPI()
router = APIRouter(
    prefix="/forms-files-errors/handling-errors",
    tags=["Formularios, ficheros y manejo de errores"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Handling Errors",
        "path": "/forms-files-errors/handling-errors",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/handling-errors/",
    }


"""
    NOTES: Handling Errors

    - Report errors using HTTPException.
    - Cuando lanzas un HTTPException, en el parámetro detail puedes
    pasarle cualquier cosa susceptible de ser convertida a JSON,
    no tiene por qué ser solo 1 str, puede ser una list, un dict, etc.
    FastAPI lo convierte automáticamente a JSON.
    - También le puedes añadir headers personalizados a la respuesta HTTP
    del error.
"""


@router.get("/item/{item_id}")
async def get_item(item_id: int) -> dict[str, int]:
    if item_id == 1:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} doesn't exist.",
            headers={"X-Error": "Yep, error"},
        )
    return {"item": item_id}


"""
    CUSTOM EXCEPTION HANDLERS

    Puedes crear tus propios manejadores de errores y manejarlos
    de manera global.
"""


# class UnicornError(Exception):
#     def __init__(self, name: str):
#         self.name = name


# @app.exception_handler(UnicornError)
# async def unicorn_exception_handler(request: Request, exc: UnicornError):
#     return JSONResponse(
#         status_code=418, content={"message": f"Oops! {exc.name} did something..."}
#     )


@router.get("/unicorn-error")
async def unicorn_error(name: str) -> dict[str, str]:
    if name == "yolo":
        raise UnicornError(name=name)
    return {"unicorn_name": name}


"""
    OVERRIDE THE DEFAULT EXCEPTION HANDLERS

    Aquellos que se encargan de devolver las respuestas JSON
    por defecto cuando se lanza una HTTPException o se recibe
    una request con datos inválidos.
    En estos próximos ejemplos se muestra cómo FastAPI
    permite modificar el tipo de respuesta, es decir,
    en vez de devolver un JSON se puede devolver un texto
    plano, útil para logs, debugging, etc.


    Override request validation exceptions:

    - Cuando una petición contiene datos inválidos,
    FastAPI lanza un RequestValidationError.
    - Para sobreescribir esta funcionalidad, solo tienes que
    decorar la función manejadora con
    @app.exception_handler(RequestValidationError), la cual
    debe recibir obligatoriamente un parámetro request y un
    exc.
    - Este tipo de excepción contiene información que puedes mostrar
    en los logs pero si conviertes el error a str y lo
    devuelves directamente, puedes estar devolviendo
    información sobre tu sistema que quizás no quieres
    mostrar. Por eso en el siguiente ejemplo se muestra
    cada error de manera independiente.
    - También hay que tener en cuenta que esto sobreescribe el
    comportamiento de la clase RequestValidationError en toda
    la aplicación, es decir, cada endpoint que reciba datos
    inválidos, devolverá este comportamiento.
"""


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     message = "Validation errors:"
#     for error in exc.errors():
#         message += f"\nField: {error['loc']}. Error: {error['msg']}"
#     return PlainTextResponse(message, status_code=400)


@router.get("/override-validation-handler/{item_id}")
async def override_validation_handler(item_id: int) -> dict[str, int]:
    if item_id == 2:
        raise HTTPException(
            status_code=418,
            detail="Nope",
        )
    return {"item": item_id}


"""
    Override the HTTPException error handler:

    - Puedes usar indistintamente las clases de errores de la librería
    Starlette.exceptions o FastAPI.exceptions. FastAPI utiliza las de
    Starlette.
    - En el caso concreto de la HTTPException de FastAPI, esta
    acepta cualquier dato que sea susceptible de ser convertido
    a JSON para el campo "detail", mientras que la de Starlette solo
    acepta strings.
    - La documentación recomienda que, cuando registres un manejador
    de excepciones para HTTPException, lo hagas con la clase
    perteneciente a Starlette porque, como FastAPI hereda de Starlette,
    si implementas un capturador de errores basado en la clase de FastAPI
    podrías estar ignorando sin querer errores lanzados por la propia
    clase de Starlette.
"""


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request: Request, exc: StarletteHTTPException):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@router.get("/override-http-handler/{item_id}")
async def override_http_handler(item_id: int):  # noqa
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}


"""
    Use the RequestValidationError body.

    - Cuando modificas el comportamiento del manejador de errores
    de validación de los datos del body de una request, puedes
    acceder a esos datos con el parámetro "body" para mostrarlos en
    logs, debugging, devolver al cliente, etc.
"""

# @app.exception_handler(RequestValidationError)
# async def override_validation_with_body_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(status_code=418, content=jsonable_encoder({
#         "detail": exc.errors(),
#         "body": exc.body
#     }))


@router.post("/override-validation-with-body")
async def override_validation_with_body(id: Annotated[int, Body()]):  # noqa
    return id


"""
    Reuse FastAPI's exception handlers

    Si quieres modificar las funciones manejadoras de errores
    por defecto de FastAPI pero que funcionen igual
    que las de por defecto, puedes reutilizarlas
    de esta manera:
"""

# @app.exception_handler(StarletteHTTPException)
# async def custom_reuse_http_exc_handler(request: Request, exc: StarletteHTTPException):
#     print(f"Reusing HTTP exception handler: {exc}")
#     return await http_exception_handler(request, exc)

# @app.exception_handler(RequestValidationError)
# async def custom_reuse_validation_exc_handler(request: Request, exc: RequestValidationError):
#     print(f"Reusing request validation exception handler: {exc}")
#     return await request_validation_exception_handler(request, exc)


@router.get("/reuse-http-exc-handler/{item_id}")
async def reuse_http_exc_handler(item_id: int):  # noqa
    if item_id == 5:
        raise HTTPException(status_code=418, detail="Nope! I don't like 5")
    return {"item_id": item_id}


@router.get("/reuse-request-validation-exc-handler/{item_id}")
async def reuse_req_validation_exc_handler(item_id: int):  # noqa
    return {"item_id": item_id}
