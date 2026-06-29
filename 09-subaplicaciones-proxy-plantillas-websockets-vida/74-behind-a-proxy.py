"""74/112 - Behind a Proxy
https://fastapi.tiangolo.com/advanced/behind-a-proxy/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/subapps-proxy-templates-websockets/behind-a-proxy", tags=["Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida",
        "lesson": "Behind a Proxy",
        "path": "/subapps-proxy-templates-websockets/behind-a-proxy",
        "reference_url": "https://fastapi.tiangolo.com/advanced/behind-a-proxy/",
    }
