"""110/112 - Configure Swagger UI
https://fastapi.tiangolo.com/how-to/configure-swagger-ui/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/configure-swagger-ui", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Configure Swagger UI",
        "path": "/how-to-recipes/configure-swagger-ui",
        "reference_url": "https://fastapi.tiangolo.com/how-to/configure-swagger-ui/",
    }
