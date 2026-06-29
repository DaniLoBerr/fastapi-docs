"""73/112 - Sub Applications - Mounts
https://fastapi.tiangolo.com/advanced/sub-applications/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/subapps-proxy-templates-websockets/sub-applications-mounts", tags=["Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida",
        "lesson": "Sub Applications - Mounts",
        "path": "/subapps-proxy-templates-websockets/sub-applications-mounts",
        "reference_url": "https://fastapi.tiangolo.com/advanced/sub-applications/",
    }
