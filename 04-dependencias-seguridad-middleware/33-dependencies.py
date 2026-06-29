"""33/111 - Dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/dependencies", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Dependencies",
        "path": "/dependencies-security-middleware/dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/",
    }
