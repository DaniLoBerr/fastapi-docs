"""103/112 - Migrate from Pydantic v1 to Pydantic v2
https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/migrate-from-pydantic-v1-to-pydantic-v2", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Migrate from Pydantic v1 to Pydantic v2",
        "path": "/how-to-recipes/migrate-from-pydantic-v1-to-pydantic-v2",
        "reference_url": "https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/",
    }
