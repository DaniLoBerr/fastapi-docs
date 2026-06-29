"""78/112 - Testing WebSockets
https://fastapi.tiangolo.com/advanced/testing-websockets/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/testing-settings-openapi/testing-websockets", tags=["Testing avanzado, settings y OpenAPI extendido"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Testing avanzado, settings y OpenAPI extendido",
        "lesson": "Testing WebSockets",
        "path": "/testing-settings-openapi/testing-websockets",
        "reference_url": "https://fastapi.tiangolo.com/advanced/testing-websockets/",
    }
