"""17/111 - Extra Data Types
https://fastapi.tiangolo.com/tutorial/extra-data-types/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/extra-data-types", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Extra Data Types",
        "path": "/user-guide/extra-data-types",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/extra-data-types/",
    }
