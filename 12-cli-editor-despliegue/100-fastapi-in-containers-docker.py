"""100/112 - FastAPI in Containers - Docker
https://fastapi.tiangolo.com/deployment/docker/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/fastapi-in-containers-docker", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "FastAPI in Containers - Docker",
        "path": "/cli-editor-deployment/fastapi-in-containers-docker",
        "reference_url": "https://fastapi.tiangolo.com/deployment/docker/",
    }
