"""90/112 - FastAPI CLI
https://fastapi.tiangolo.com/fastapi-cli/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/fastapi-cli", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "FastAPI CLI",
        "path": "/cli-editor-deployment/fastapi-cli",
        "reference_url": "https://fastapi.tiangolo.com/fastapi-cli/",
    }
