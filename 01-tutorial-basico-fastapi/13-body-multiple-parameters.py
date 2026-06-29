"""13/111 - Body - Multiple Parameters
https://fastapi.tiangolo.com/tutorial/body-multiple-params/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/body-multiple-parameters", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Body - Multiple Parameters",
        "path": "/user-guide/body-multiple-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-multiple-params/",
    }
