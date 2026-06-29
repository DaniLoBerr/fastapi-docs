"""47/111 - Bigger Applications - Multiple Files
https://fastapi.tiangolo.com/tutorial/bigger-applications/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/sql-apps-background/bigger-applications-multiple-files", tags=["BBDD SQL, estructura de apps grandes y tareas en segundo plano"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "BBDD SQL, estructura de apps grandes y tareas en segundo plano",
        "lesson": "Bigger Applications - Multiple Files",
        "path": "/sql-apps-background/bigger-applications-multiple-files",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/bigger-applications/",
    }
