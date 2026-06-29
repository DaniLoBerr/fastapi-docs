"""23/111 - Extra Models
https://fastapi.tiangolo.com/tutorial/extra-models/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/special-params/extra-models", tags=["Parámetros especiales, modelos en capas y respuestas"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Extra Models",
        "path": "/special-params/extra-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/extra-models/",
    }
