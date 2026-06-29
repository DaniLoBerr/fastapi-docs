"""45/111 - CORS (Cross-Origin Resource Sharing)
https://fastapi.tiangolo.com/tutorial/cors/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/cors", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "CORS (Cross-Origin Resource Sharing)",
        "path": "/dependencies-security-middleware/cors",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/cors/",
    }
