"""5/111 - Tutorial - User Guide
https://fastapi.tiangolo.com/tutorial/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user-guide/tutorial-user-guide", tags=["Tutorial Básico de FastAPI"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Tutorial - User Guide",
        "path": "/user-guide/tutorial-user-guide",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/",
    }
