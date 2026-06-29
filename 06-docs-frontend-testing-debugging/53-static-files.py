"""53/112 - Static Files
https://fastapi.tiangolo.com/tutorial/static-files/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/docs-frontend-testing-debugging/static-files", tags=["Docs, frontend estático, testing y debugging"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Docs, frontend estático, testing y debugging",
        "lesson": "Static Files",
        "path": "/docs-frontend-testing-debugging/static-files",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/static-files/",
    }
