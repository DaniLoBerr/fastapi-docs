"""51/112 - Metadata and Docs URLs
https://fastapi.tiangolo.com/tutorial/metadata/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/docs-frontend-testing-debugging/metadata-and-docs-urls", tags=["Docs, frontend estático, testing y debugging"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Docs, frontend estático, testing y debugging",
        "lesson": "Metadata and Docs URLs",
        "path": "/docs-frontend-testing-debugging/metadata-and-docs-urls",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/metadata/",
    }
