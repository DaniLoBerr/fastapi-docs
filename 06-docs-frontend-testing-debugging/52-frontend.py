"""52/112 - Frontend
https://fastapi.tiangolo.com/tutorial/frontend/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/docs-frontend-testing-debugging/frontend", tags=["Docs, frontend estático, testing y debugging"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Docs, frontend estático, testing y debugging",
        "lesson": "Frontend",
        "path": "/docs-frontend-testing-debugging/frontend",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/frontend/",
    }
