"""12/111 - Query Parameter Models
https://fastapi.tiangolo.com/tutorial/query-param-models/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/query-parameter-models", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Query Parameter Models",
        "path": "/user-guide/query-parameter-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/query-param-models/",
    }
