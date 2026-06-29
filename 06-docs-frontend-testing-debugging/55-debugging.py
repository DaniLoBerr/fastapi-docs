"""55/112 - Debugging
https://fastapi.tiangolo.com/tutorial/debugging/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/docs-frontend-testing-debugging/debugging", tags=["Docs, frontend estático, testing y debugging"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Docs, frontend estático, testing y debugging",
        "lesson": "Debugging",
        "path": "/docs-frontend-testing-debugging/debugging",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/debugging/",
    }
