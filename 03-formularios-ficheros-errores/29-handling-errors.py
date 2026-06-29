"""29/111 - Handling Errors
https://fastapi.tiangolo.com/tutorial/handling-errors/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/handling-errors", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Handling Errors",
        "path": "/forms-files-errors/handling-errors",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/handling-errors/",
    }
