"""61/112 - Custom Response - HTML, Stream, File, others
https://fastapi.tiangolo.com/advanced/custom-response/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/custom-response-html-stream-file-others", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Custom Response - HTML, Stream, File, others",
        "path": "/advanced-user-guide/custom-response-html-stream-file-others",
        "reference_url": "https://fastapi.tiangolo.com/advanced/custom-response/",
    }
