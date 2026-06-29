"""16/111 - Declare Request Example Data
https://fastapi.tiangolo.com/tutorial/schema-extra-example/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/declare-request-example-data", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Declare Request Example Data",
        "path": "/user-guide/declare-request-example-data",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/schema-extra-example/",
    }
