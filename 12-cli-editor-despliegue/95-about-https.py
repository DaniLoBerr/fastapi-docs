"""95/112 - About HTTPS
https://fastapi.tiangolo.com/deployment/https/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/about-https", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "About HTTPS",
        "path": "/cli-editor-deployment/about-https",
        "reference_url": "https://fastapi.tiangolo.com/deployment/https/",
    }
