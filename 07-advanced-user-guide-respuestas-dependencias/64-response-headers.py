"""64/112 - Response Headers
https://fastapi.tiangolo.com/advanced/response-headers/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/response-headers", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Response Headers",
        "path": "/advanced-user-guide/response-headers",
        "reference_url": "https://fastapi.tiangolo.com/advanced/response-headers/",
    }
