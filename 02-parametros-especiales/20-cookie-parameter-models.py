"""20/111 - Cookie Parameter Models
https://fastapi.tiangolo.com/tutorial/cookie-param-models/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/special-params/cookie-parameter-models", tags=["Parámetros especiales, modelos en capas y respuestas"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Cookie Parameter Models",
        "path": "/special-params/cookie-parameter-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/cookie-param-models/",
    }
