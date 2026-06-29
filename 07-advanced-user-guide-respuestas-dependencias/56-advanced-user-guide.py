"""56/112 - Advanced User Guide
https://fastapi.tiangolo.com/advanced/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/advanced-user-guide", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Advanced User Guide",
        "path": "/advanced-user-guide/advanced-user-guide",
        "reference_url": "https://fastapi.tiangolo.com/advanced/",
    }
