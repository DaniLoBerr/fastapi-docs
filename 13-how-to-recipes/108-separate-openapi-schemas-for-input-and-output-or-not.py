"""108/112 - Separate OpenAPI Schemas for Input and Output or Not
https://fastapi.tiangolo.com/how-to/separate-openapi-schemas/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/separate-openapi-schemas-for-input-and-output-or-not", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Separate OpenAPI Schemas for Input and Output or Not",
        "path": "/how-to-recipes/separate-openapi-schemas-for-input-and-output-or-not",
        "reference_url": "https://fastapi.tiangolo.com/how-to/separate-openapi-schemas/",
    }
