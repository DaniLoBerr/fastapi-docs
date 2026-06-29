"""25/111 - Form Data
https://fastapi.tiangolo.com/tutorial/request-forms/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/form-data", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Form Data",
        "path": "/forms-files-errors/form-data",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-forms/",
    }
