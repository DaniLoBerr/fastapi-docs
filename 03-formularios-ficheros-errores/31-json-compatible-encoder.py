"""31/111 - JSON Compatible Encoder
https://fastapi.tiangolo.com/tutorial/encoder/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/json-compatible-encoder", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "JSON Compatible Encoder",
        "path": "/forms-files-errors/json-compatible-encoder",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/encoder/",
    }
