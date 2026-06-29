"""111/112 - Testing a Database
https://fastapi.tiangolo.com/how-to/testing-database/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/testing-a-database", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Testing a Database",
        "path": "/how-to-recipes/testing-a-database",
        "reference_url": "https://fastapi.tiangolo.com/how-to/testing-database/",
    }
