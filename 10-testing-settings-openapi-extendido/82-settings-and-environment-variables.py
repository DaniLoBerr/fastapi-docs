"""82/112 - Settings and Environment Variables
https://fastapi.tiangolo.com/advanced/settings/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/testing-settings-openapi/settings-and-environment-variables", tags=["Testing avanzado, settings y OpenAPI extendido"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Testing avanzado, settings y OpenAPI extendido",
        "lesson": "Settings and Environment Variables",
        "path": "/testing-settings-openapi/settings-and-environment-variables",
        "reference_url": "https://fastapi.tiangolo.com/advanced/settings/",
    }
