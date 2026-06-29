"""14/111 - Body - Fields
https://fastapi.tiangolo.com/tutorial/body-fields/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/body-fields", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Body - Fields",
        "path": "/user-guide/body-fields",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-fields/",
    }
