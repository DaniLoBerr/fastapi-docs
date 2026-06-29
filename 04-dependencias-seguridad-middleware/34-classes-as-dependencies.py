"""34/111 - Classes as Dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/classes-as-dependencies", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Classes as Dependencies",
        "path": "/dependencies-security-middleware/classes-as-dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/",
    }
