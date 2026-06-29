"""30/111 - Path Operation Configuration
https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/path-operation-configuration", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Path Operation Configuration",
        "path": "/forms-files-errors/path-operation-configuration",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/path-operation-configuration/",
    }
