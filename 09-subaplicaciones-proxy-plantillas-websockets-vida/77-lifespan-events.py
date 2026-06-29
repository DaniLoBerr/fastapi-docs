"""77/112 - Lifespan Events
https://fastapi.tiangolo.com/advanced/events/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/subapps-proxy-templates-websockets/lifespan-events", tags=["Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida",
        "lesson": "Lifespan Events",
        "path": "/subapps-proxy-templates-websockets/lifespan-events",
        "reference_url": "https://fastapi.tiangolo.com/advanced/events/",
    }
