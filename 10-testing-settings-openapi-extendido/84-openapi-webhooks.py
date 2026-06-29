"""84/112 - OpenAPI Webhooks
https://fastapi.tiangolo.com/advanced/openapi-webhooks/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/testing-settings-openapi/openapi-webhooks", tags=["Testing avanzado, settings y OpenAPI extendido"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Testing avanzado, settings y OpenAPI extendido",
        "lesson": "OpenAPI Webhooks",
        "path": "/testing-settings-openapi/openapi-webhooks",
        "reference_url": "https://fastapi.tiangolo.com/advanced/openapi-webhooks/",
    }
