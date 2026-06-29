"""48/111 - Stream JSON Lines
https://fastapi.tiangolo.com/tutorial/stream-json-lines/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/sql-apps-background/stream-json-lines", tags=["BBDD SQL, estructura de apps grandes y tareas en segundo plano"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "BBDD SQL, estructura de apps grandes y tareas en segundo plano",
        "lesson": "Stream JSON Lines",
        "path": "/sql-apps-background/stream-json-lines",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/stream-json-lines/",
    }
