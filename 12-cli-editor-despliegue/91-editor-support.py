"""91/112 - Editor Support
https://fastapi.tiangolo.com/editor-support/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/editor-support", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "Editor Support",
        "path": "/cli-editor-deployment/editor-support",
        "reference_url": "https://fastapi.tiangolo.com/editor-support/",
    }
