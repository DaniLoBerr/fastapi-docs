"""19/111 - Header Parameters
https://fastapi.tiangolo.com/tutorial/header-params/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/special-params/header-parameters", tags=["Parámetros especiales, modelos en capas y respuestas"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Header Parameters",
        "path": "/special-params/header-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/header-params/",
    }
