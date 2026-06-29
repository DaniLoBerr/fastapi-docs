"""49/111 - Server-Sent Events (SSE)
https://fastapi.tiangolo.com/tutorial/server-sent-events/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/sql-apps-background/server-sent-events-sse", tags=["BBDD SQL, estructura de apps grandes y tareas en segundo plano"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "BBDD SQL, estructura de apps grandes y tareas en segundo plano",
        "lesson": "Server-Sent Events (SSE)",
        "path": "/sql-apps-background/server-sent-events-sse",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/server-sent-events/",
    }
