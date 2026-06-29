"""27/111 - Request Files
https://fastapi.tiangolo.com/tutorial/request-files/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/request-files", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Request Files",
        "path": "/forms-files-errors/request-files",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-files/",
    }
