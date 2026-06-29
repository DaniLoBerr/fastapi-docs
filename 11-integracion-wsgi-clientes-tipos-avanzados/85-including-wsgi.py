"""85/112 - Including WSGI - Flask, Django, others
https://fastapi.tiangolo.com/advanced/wsgi/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/integration-wsgi-generating-clients/including-wsgi", tags=["Integración con WSGI, generación de clientes y tipos avanzados"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Integración con WSGI, generación de clientes y tipos avanzados",
        "lesson": "Including WSGI - Flask, Django, others",
        "path": "/integration-wsgi-generating-clients/including-wsgi",
        "reference_url": "https://fastapi.tiangolo.com/advanced/wsgi/",
    }
