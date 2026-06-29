"""62/112 - Additional Responses in OpenAPI
https://fastapi.tiangolo.com/advanced/additional-responses/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/advanced-user-guide/additional-responses-in-openapi", tags=["Advanced User Guide"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lesson": "Additional Responses in OpenAPI",
        "path": "/advanced-user-guide/additional-responses-in-openapi",
        "reference_url": "https://fastapi.tiangolo.com/advanced/additional-responses/",
    }
