"""70/112 - Using the Request Directly
https://fastapi.tiangolo.com/advanced/using-request-directly/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-security/using-the-request-directly", tags=["Advanced Security"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced Security y middlewares",
        "lesson": "Using the Request Directly",
        "path": "/advanced-security/using-the-request-directly",
        "reference_url": "https://fastapi.tiangolo.com/advanced/using-request-directly/",
    }
