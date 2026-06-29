"""87/112 - Advanced Python Types
https://fastapi.tiangolo.com/advanced/advanced-python-types/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/integration-wsgi-generating-clients/advanced-python-types", tags=["Integración con WSGI, generación de clientes y tipos avanzados"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Integración con WSGI, generación de clientes y tipos avanzados",
        "lesson": "Advanced Python Types",
        "path": "/integration-wsgi-generating-clients/advanced-python-types",
        "reference_url": "https://fastapi.tiangolo.com/advanced/advanced-python-types/",
    }
