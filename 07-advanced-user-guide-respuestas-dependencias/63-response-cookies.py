"""63/112 - Response Cookies
https://fastapi.tiangolo.com/advanced/response-cookies/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/response-cookies", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Response Cookies",
        "path": "/advanced-user-guide/response-cookies",
        "reference_url": "https://fastapi.tiangolo.com/advanced/response-cookies/",
    }
