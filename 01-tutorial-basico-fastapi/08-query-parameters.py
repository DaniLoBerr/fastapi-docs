"""8/111 - Query Parameters
https://fastapi.tiangolo.com/tutorial/query-params/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/query-parameters", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Query Parameters",
        "path": "/user-guide/query-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/query-params/",
    }
