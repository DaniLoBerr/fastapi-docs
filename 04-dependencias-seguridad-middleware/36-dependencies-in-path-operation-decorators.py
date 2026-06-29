"""36/111 - Dependencies in path operation decorators
https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/dependencies-security-middleware/dependencies-in-path-operation-decorators", tags=["Dependencias, seguridad básica y middleware"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Dependencies in path operation decorators",
        "path": "/dependencies-security-middleware/dependencies-in-path-operation-decorators",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/",
    }
