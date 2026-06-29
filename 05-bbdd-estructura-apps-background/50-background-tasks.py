"""50/111 - Background Tasks
https://fastapi.tiangolo.com/tutorial/background-tasks/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/sql-apps-background/background-tasks", tags=["BBDD SQL, estructura de apps grandes y tareas en segundo plano"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "BBDD SQL, estructura de apps grandes y tareas en segundo plano",
        "lesson": "Background Tasks",
        "path": "/sql-apps-background/background-tasks",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/background-tasks/",
    }
