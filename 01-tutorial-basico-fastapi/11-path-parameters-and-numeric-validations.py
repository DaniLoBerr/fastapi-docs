"""11/111 - Path Parameters and Numeric Validations
https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/path-parameters-and-numeric-validations", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Path Parameters and Numeric Validations",
        "path": "/user-guide/path-parameters-and-numeric-validations",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/",
    }
