"""89/112 - Strict Content-Type Checking
https://fastapi.tiangolo.com/advanced/strict-content-type/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/integration-wsgi-generating-clients/strict-content-type-checking", tags=["Integración con WSGI, generación de clientes y tipos avanzados"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Integración con WSGI, generación de clientes y tipos avanzados",
        "lesson": "Strict Content-Type Checking",
        "path": "/integration-wsgi-generating-clients/strict-content-type-checking",
        "reference_url": "https://fastapi.tiangolo.com/advanced/strict-content-type/",
    }
