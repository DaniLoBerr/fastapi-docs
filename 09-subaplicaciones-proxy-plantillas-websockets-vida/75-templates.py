"""75/112 - Templates
https://fastapi.tiangolo.com/advanced/templates/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/subapps-proxy-templates-websockets/templates", tags=["Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida",
        "lesson": "Templates",
        "path": "/subapps-proxy-templates-websockets/templates",
        "reference_url": "https://fastapi.tiangolo.com/advanced/templates/",
    }
