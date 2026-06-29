"""93/112 - About FastAPI versions
https://fastapi.tiangolo.com/deployment/versions/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/about-fastapi-versions", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "About FastAPI versions",
        "path": "/cli-editor-deployment/about-fastapi-versions",
        "reference_url": "https://fastapi.tiangolo.com/deployment/versions/",
    }
