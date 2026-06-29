"""67/112 - Advanced Security
https://fastapi.tiangolo.com/advanced/security/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-security/advanced-security", tags=["Advanced Security"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced Security y middlewares",
        "lesson": "Advanced Security",
        "path": "/advanced-security/advanced-security",
        "reference_url": "https://fastapi.tiangolo.com/advanced/security/",
    }
