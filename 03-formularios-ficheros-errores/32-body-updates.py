"""32/111 - Body - Updates
https://fastapi.tiangolo.com/tutorial/body-updates/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/forms-files-errors/body-updates", tags=["Formularios, ficheros y manejo de errores"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Body - Updates",
        "path": "/forms-files-errors/body-updates",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-updates/",
    }
