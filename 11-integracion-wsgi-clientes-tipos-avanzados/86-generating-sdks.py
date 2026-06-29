"""86/112 - Generating SDKs
https://fastapi.tiangolo.com/advanced/generate-clients/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/integration-wsgi-generating-clients/generating-sdks", tags=["Integración con WSGI, generación de clientes y tipos avanzados"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Integración con WSGI, generación de clientes y tipos avanzados",
        "lesson": "Generating SDKs",
        "path": "/integration-wsgi-generating-clients/generating-sdks",
        "reference_url": "https://fastapi.tiangolo.com/advanced/generate-clients/",
    }
