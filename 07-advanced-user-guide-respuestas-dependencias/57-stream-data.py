"""57/112 - Stream Data
https://fastapi.tiangolo.com/advanced/stream-data/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/stream-data", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Stream Data",
        "path": "/advanced-user-guide/stream-data",
        "reference_url": "https://fastapi.tiangolo.com/advanced/stream-data/",
    }
