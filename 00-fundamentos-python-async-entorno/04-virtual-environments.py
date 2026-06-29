"""4/111 - Virtual Environments
https://fastapi.tiangolo.com/virtual-environments/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/foundations/virtual-environments", tags=["Fundamentos de Python, async y entorno"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Fundamentos de Python, async y entorno",
        "lesson": "Virtual Environments",
        "path": "/foundations/virtual-environments",
        "reference_url": "https://fastapi.tiangolo.com/virtual-environments/",
    }
