from fastapi import FastAPI
from routers import routers

app = FastAPI()

for router in routers:
    app.include_router(router)


@app.get("/")
def read_root():
    return {"Title": "Welcome to danilober's FastAPI tutorial notes!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
