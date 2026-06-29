"""35/111 - Sub-dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/sub-dependencies", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Sub-dependencies",
        "path": "/dependencies-security-middleware/sub-dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/",
    }
