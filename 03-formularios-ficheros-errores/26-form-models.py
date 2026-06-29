"""26/111 - Form Models
https://fastapi.tiangolo.com/tutorial/request-form-models/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/form-models", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Form Models",
        "path": "/forms-files-errors/form-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-form-models/",
    }
