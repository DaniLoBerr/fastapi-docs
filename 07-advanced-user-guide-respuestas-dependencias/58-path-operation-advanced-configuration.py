"""58/112 - Path Operation Advanced Configuration
https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/path-operation-advanced-configuration", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Path Operation Advanced Configuration",
        "path": "/advanced-user-guide/path-operation-advanced-configuration",
        "reference_url": "https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/",
    }
