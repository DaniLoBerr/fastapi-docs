"""42/111 - Simple OAuth2 with Password and Bearer
https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/simple-oauth2-with-password-and-bearer", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Simple OAuth2 with Password and Bearer",
        "path": "/dependencies-security-middleware/simple-oauth2-with-password-and-bearer",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/",
    }
