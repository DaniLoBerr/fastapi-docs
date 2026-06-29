"""101/112 - How To - Recipes
https://fastapi.tiangolo.com/how-to/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/how-to-recipes", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "How To - Recipes",
        "path": "/how-to-recipes/how-to-recipes",
        "reference_url": "https://fastapi.tiangolo.com/how-to/",
    }
