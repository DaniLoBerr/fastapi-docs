"""40/111 - Security - First Steps
https://fastapi.tiangolo.com/tutorial/security/first-steps/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/security-first-steps", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Security - First Steps",
        "path": "/dependencies-security-middleware/security-first-steps",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/first-steps/",
    }
