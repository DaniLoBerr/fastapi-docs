"""43/111 - OAuth2 with Password (and hashing), Bearer with JWT tokens
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/oauth2-with-password-and-bearer-jwt-tokens", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "OAuth2 with Password (and hashing), Bearer with JWT tokens",
        "path": "/dependencies-security-middleware/oauth2-with-password-and-bearer-jwt-tokens",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/",
    }
