"""59/112 - Additional Status Codes
https://fastapi.tiangolo.com/advanced/additional-status-codes/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/additional-status-codes", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Additional Status Codes",
        "path": "/advanced-user-guide/additional-status-codes",
        "reference_url": "https://fastapi.tiangolo.com/advanced/additional-status-codes/",
    }
