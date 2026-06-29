"""28/111 - Request Forms and Files
https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/request-forms-and-files", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Request Forms and Files",
        "path": "/forms-files-errors/request-forms-and-files",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-forms-and-files/",
    }
