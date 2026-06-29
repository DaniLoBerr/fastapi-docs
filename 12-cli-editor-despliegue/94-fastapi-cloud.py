"""94/112 - FastAPI Cloud
https://fastapi.tiangolo.com/deployment/fastapicloud/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/fastapi-cloud", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "FastAPI Cloud",
        "path": "/cli-editor-deployment/fastapi-cloud",
        "reference_url": "https://fastapi.tiangolo.com/deployment/fastapicloud/",
    }
