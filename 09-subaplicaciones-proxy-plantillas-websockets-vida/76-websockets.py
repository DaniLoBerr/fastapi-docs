"""76/112 - WebSockets
https://fastapi.tiangolo.com/advanced/websockets/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/subapps-proxy-templates-websockets/websockets", tags=["Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida",
        "lesson": "WebSockets",
        "path": "/subapps-proxy-templates-websockets/websockets",
        "reference_url": "https://fastapi.tiangolo.com/advanced/websockets/",
    }
