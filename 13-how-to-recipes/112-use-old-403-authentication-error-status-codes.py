"""112/112 - Use Old 403 Authentication Error Status Codes
https://fastapi.tiangolo.com/how-to/authentication-error-status-code/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/use-old-403-authentication-error-status-codes", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "Use Old 403 Authentication Error Status Codes",
        "path": "/how-to-recipes/use-old-403-authentication-error-status-codes",
        "reference_url": "https://fastapi.tiangolo.com/how-to/authentication-error-status-code/",
    }
