"""69/112 - HTTP Basic Auth
https://fastapi.tiangolo.com/advanced/security/http-basic-auth/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-security/http-basic-auth", tags=["Advanced Security"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced Security y middlewares",
        "lesson": "HTTP Basic Auth",
        "path": "/advanced-security/http-basic-auth",
        "reference_url": "https://fastapi.tiangolo.com/advanced/security/http-basic-auth/",
    }
