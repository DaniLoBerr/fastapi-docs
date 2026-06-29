"""83/112 - OpenAPI Callbacks
https://fastapi.tiangolo.com/advanced/openapi-callbacks/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/testing-settings-openapi/openapi-callbacks", tags=["Testing avanzado, settings y OpenAPI extendido"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Testing avanzado, settings y OpenAPI extendido",
        "lesson": "OpenAPI Callbacks",
        "path": "/testing-settings-openapi/openapi-callbacks",
        "reference_url": "https://fastapi.tiangolo.com/advanced/openapi-callbacks/",
    }
