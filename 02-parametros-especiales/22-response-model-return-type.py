"""22/111 - Response Model - Return Type
https://fastapi.tiangolo.com/tutorial/response-model/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/special-params/response-model-return-type", tags=["Parámetros especiales, modelos en capas y respuestas"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Response Model - Return Type",
        "path": "/special-params/response-model-return-type",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/response-model/",
    }
