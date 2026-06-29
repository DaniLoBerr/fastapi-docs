"""97/112 - Deployments Concepts
https://fastapi.tiangolo.com/deployment/concepts/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/deployments-concepts", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "Deployments Concepts",
        "path": "/cli-editor-deployment/deployments-concepts",
        "reference_url": "https://fastapi.tiangolo.com/deployment/concepts/",
    }
