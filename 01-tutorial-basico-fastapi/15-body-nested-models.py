"""15/111 - Body - Nested Models
https://fastapi.tiangolo.com/tutorial/body-nested-models/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/body-nested-models", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Body - Nested Models",
        "path": "/user-guide/body-nested-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-nested-models/",
    }
