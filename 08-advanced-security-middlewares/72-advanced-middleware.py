"""72/112 - Advanced Middleware
https://fastapi.tiangolo.com/advanced/middleware/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-security/advanced-middleware", tags=["Advanced Security"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced Security y middlewares",
        "lesson": "Advanced Middleware",
        "path": "/advanced-security/advanced-middleware",
        "reference_url": "https://fastapi.tiangolo.com/advanced/middleware/",
    }
