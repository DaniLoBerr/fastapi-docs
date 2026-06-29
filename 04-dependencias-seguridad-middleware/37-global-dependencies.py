"""37/111 - Global Dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/global-dependencies", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Global Dependencies",
        "path": "/dependencies-security-middleware/global-dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/",
    }
