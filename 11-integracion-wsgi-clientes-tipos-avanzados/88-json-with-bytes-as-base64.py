"""88/112 - JSON with Bytes as Base64
https://fastapi.tiangolo.com/advanced/json-base64-bytes/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/integration-wsgi-generating-clients/json-with-bytes-as-base64", tags=["Integración con WSGI, generación de clientes y tipos avanzados"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Integración con WSGI, generación de clientes y tipos avanzados",
        "lesson": "JSON with Bytes as Base64",
        "path": "/integration-wsgi-generating-clients/json-with-bytes-as-base64",
        "reference_url": "https://fastapi.tiangolo.com/advanced/json-base64-bytes/",
    }
