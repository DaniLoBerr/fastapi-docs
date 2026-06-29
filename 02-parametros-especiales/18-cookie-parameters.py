"""18/111 - Cookie Parameters
https://fastapi.tiangolo.com/tutorial/cookie-params/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/special-params/cookie-parameters", tags=["Parámetros especiales, modelos en capas y respuestas"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Cookie Parameters",
        "path": "/special-params/cookie-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/cookie-params/",
    }
