"""80/112 - Testing Dependencies with Overrides
https://fastapi.tiangolo.com/advanced/testing-dependencies/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/testing-settings-openapi/testing-dependencies-with-overrides", tags=["Testing avanzado, settings y OpenAPI extendido"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Testing avanzado, settings y OpenAPI extendido",
        "lesson": "Testing Dependencies with Overrides",
        "path": "/testing-settings-openapi/testing-dependencies-with-overrides",
        "reference_url": "https://fastapi.tiangolo.com/advanced/testing-dependencies/",
    }
