"""107/112 - Extending OpenAPI
https://fastapi.tiangolo.com/how-to/extending-openapi/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/extending-openapi", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Extending OpenAPI",
        "path": "/how-to-recipes/extending-openapi",
        "reference_url": "https://fastapi.tiangolo.com/how-to/extending-openapi/",
    }
