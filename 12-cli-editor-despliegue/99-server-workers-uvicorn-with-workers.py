"""99/112 - Server Workers - Uvicorn with Workers
https://fastapi.tiangolo.com/deployment/server-workers/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/server-workers-uvicorn-with-workers", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "Server Workers - Uvicorn with Workers",
        "path": "/cli-editor-deployment/server-workers-uvicorn-with-workers",
        "reference_url": "https://fastapi.tiangolo.com/deployment/server-workers/",
    }
