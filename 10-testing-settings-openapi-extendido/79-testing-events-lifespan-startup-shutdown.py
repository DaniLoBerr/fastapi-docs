"""79/112 - Testing Events: lifespan and startup - shutdown
https://fastapi.tiangolo.com/advanced/testing-events/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/testing-settings-openapi/testing-events-lifespan-startup-shutdown", tags=["Testing avanzado, settings y OpenAPI extendido"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Testing avanzado, settings y OpenAPI extendido",
        "lesson": "Testing Events: lifespan and startup - shutdown",
        "path": "/testing-settings-openapi/testing-events-lifespan-startup-shutdown",
        "reference_url": "https://fastapi.tiangolo.com/advanced/testing-events/",
    }
