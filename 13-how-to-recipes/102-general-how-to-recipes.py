"""102/112 - General - How To - Recipes
https://fastapi.tiangolo.com/how-to/general/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/general-how-to-recipes", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "General - How To - Recipes",
        "path": "/how-to-recipes/general-how-to-recipes",
        "reference_url": "https://fastapi.tiangolo.com/how-to/general/",
    }
