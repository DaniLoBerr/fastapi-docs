"""44/111 - Middleware
https://fastapi.tiangolo.com/tutorial/middleware/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/middleware", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Middleware",
        "path": "/dependencies-security-middleware/middleware",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/middleware/",
    }
