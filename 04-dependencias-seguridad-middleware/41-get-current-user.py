"""41/111 - Get Current User
https://fastapi.tiangolo.com/tutorial/security/get-current-user/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/get-current-user", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Get Current User",
        "path": "/dependencies-security-middleware/get-current-user",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/get-current-user/",
    }
