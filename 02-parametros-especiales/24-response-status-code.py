"""24/111 - Response Status Code
https://fastapi.tiangolo.com/tutorial/response-status-code/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/special-params/response-status-code", tags=["Parámetros especiales, modelos en capas y respuestas"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Response Status Code",
        "path": "/special-params/response-status-code",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/response-status-code/",
    }
