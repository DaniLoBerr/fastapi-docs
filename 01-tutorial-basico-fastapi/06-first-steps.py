"""6/111 - First Steps
https://fastapi.tiangolo.com/tutorial/first-steps/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/first-steps", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "First Steps",
        "path": "/user-guide/first-steps",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/first-steps/",
    }
