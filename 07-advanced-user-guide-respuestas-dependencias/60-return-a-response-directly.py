"""60/112 - Return a Response Directly
https://fastapi.tiangolo.com/advanced/response-directly/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/return-a-response-directly", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Return a Response Directly",
        "path": "/advanced-user-guide/return-a-response-directly",
        "reference_url": "https://fastapi.tiangolo.com/advanced/response-directly/",
    }
