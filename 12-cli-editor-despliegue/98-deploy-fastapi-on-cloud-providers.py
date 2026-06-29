"""98/112 - Deploy FastAPI on Cloud Providers
https://fastapi.tiangolo.com/deployment/cloud/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/deploy-fastapi-on-cloud-providers", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "Deploy FastAPI on Cloud Providers",
        "path": "/cli-editor-deployment/deploy-fastapi-on-cloud-providers",
        "reference_url": "https://fastapi.tiangolo.com/deployment/cloud/",
    }
