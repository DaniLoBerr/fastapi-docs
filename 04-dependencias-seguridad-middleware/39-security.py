"""39/111 - Security
https://fastapi.tiangolo.com/tutorial/security/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/security", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Security",
        "path": "/dependencies-security-middleware/security",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/",
    }
