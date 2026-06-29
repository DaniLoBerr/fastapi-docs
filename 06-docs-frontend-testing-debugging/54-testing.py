"""54/112 - Testing
https://fastapi.tiangolo.com/tutorial/testing/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/docs-frontend-testing-debugging/testing", tags=["Docs, frontend estático, testing y debugging"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Docs, frontend estático, testing y debugging",
        "lesson": "Testing",
        "path": "/docs-frontend-testing-debugging/testing",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/testing/",
    }
