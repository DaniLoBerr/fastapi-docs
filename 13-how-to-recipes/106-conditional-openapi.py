"""106/112 - Conditional OpenAPI
https://fastapi.tiangolo.com/how-to/conditional-openapi/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/conditional-openapi", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Conditional OpenAPI",
        "path": "/how-to-recipes/conditional-openapi",
        "reference_url": "https://fastapi.tiangolo.com/how-to/conditional-openapi/",
    }
