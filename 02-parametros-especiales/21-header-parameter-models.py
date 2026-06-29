"""21/111 - Header Parameter Models
https://fastapi.tiangolo.com/tutorial/header-param-models/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/special-params/header-parameter-models", tags=["Parámetros especiales, modelos en capas y respuestas"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Header Parameter Models",
        "path": "/special-params/header-parameter-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/header-param-models/",
    }
