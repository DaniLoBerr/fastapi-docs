"""68/112 - OAuth2 scopes
https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-security/oauth2-scopes", tags=["Advanced Security"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced Security y middlewares",
        "lesson": "OAuth2 scopes",
        "path": "/advanced-security/oauth2-scopes",
        "reference_url": "https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/",
    }
