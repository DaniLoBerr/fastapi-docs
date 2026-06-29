"""10/111 - Query Parameters and String Validations
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/query-parameters-and-string-validations", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Query Parameters and String Validations",
        "path": "/user-guide/query-parameters-and-string-validations",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/query-params-str-validations/",
    }
