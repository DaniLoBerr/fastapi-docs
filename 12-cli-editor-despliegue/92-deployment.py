"""92/112 - Deployment
https://fastapi.tiangolo.com/deployment/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/deployment", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "Deployment",
        "path": "/cli-editor-deployment/deployment",
        "reference_url": "https://fastapi.tiangolo.com/deployment/",
    }
