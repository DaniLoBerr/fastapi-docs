"""81/112 - Async Tests
https://fastapi.tiangolo.com/advanced/async-tests/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/testing-settings-openapi/async-tests", tags=["Testing avanzado, settings y OpenAPI extendido"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Testing avanzado, settings y OpenAPI extendido",
        "lesson": "Async Tests",
        "path": "/testing-settings-openapi/async-tests",
        "reference_url": "https://fastapi.tiangolo.com/advanced/async-tests/",
    }
