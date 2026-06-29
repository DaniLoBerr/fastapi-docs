"""71/112 - Using Dataclasses
https://fastapi.tiangolo.com/advanced/dataclasses/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-security/using-dataclasses", tags=["Advanced Security"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced Security y middlewares",
        "lesson": "Using Dataclasses",
        "path": "/advanced-security/using-dataclasses",
        "reference_url": "https://fastapi.tiangolo.com/advanced/dataclasses/",
    }
