"""105/112 - Custom Request and APIRoute class
https://fastapi.tiangolo.com/how-to/custom-request-and-route/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/custom-request-and-apiroute-class", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Custom Request and APIRoute class",
        "path": "/how-to-recipes/custom-request-and-apiroute-class",
        "reference_url": "https://fastapi.tiangolo.com/how-to/custom-request-and-route/",
    }
