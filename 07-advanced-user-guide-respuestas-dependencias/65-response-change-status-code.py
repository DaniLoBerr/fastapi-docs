"""65/112 - Response - Change Status Code
https://fastapi.tiangolo.com/advanced/response-change-status-code/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/response-change-status-code", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Response - Change Status Code",
        "path": "/advanced-user-guide/response-change-status-code",
        "reference_url": "https://fastapi.tiangolo.com/advanced/response-change-status-code/",
    }
