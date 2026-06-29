"""38/111 - Dependencies with yield
https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/dependencies-with-yield", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Dependencies with yield",
        "path": "/dependencies-security-middleware/dependencies-with-yield",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/",
    }
