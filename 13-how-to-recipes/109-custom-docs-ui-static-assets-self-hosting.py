"""109/112 - Custom Docs UI Static Assets (Self-Hosting)
https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/custom-docs-ui-static-assets-self-hosting", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Custom Docs UI Static Assets (Self-Hosting)",
        "path": "/how-to-recipes/custom-docs-ui-static-assets-self-hosting",
        "reference_url": "https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/",
    }
