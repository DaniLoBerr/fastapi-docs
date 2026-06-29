"""46/111 - SQL (Relational) Databases
https://fastapi.tiangolo.com/tutorial/sql-databases/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/sql-apps-background/sql-databases", tags=["BBDD SQL, estructura de apps grandes y tareas en segundo plano"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "BBDD SQL, estructura de apps grandes y tareas en segundo plano",
        "lesson": "SQL (Relational) Databases",
        "path": "/sql-apps-background/sql-databases",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/sql-databases/",
    }
