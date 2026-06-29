"""66/112 - Advanced Dependencies
https://fastapi.tiangolo.com/advanced/advanced-dependencies/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/advanced-dependencies", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Advanced Dependencies",
        "path": "/advanced-user-guide/advanced-dependencies",
        "reference_url": "https://fastapi.tiangolo.com/advanced/advanced-dependencies/",
    }
