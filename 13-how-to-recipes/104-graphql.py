"""104/112 - GraphQL
https://fastapi.tiangolo.com/how-to/graphql/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/how-to-recipes/graphql", tags=["How To - Recipes"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "How To / Recipes",
        "lesson": "GraphQL",
        "path": "/how-to-recipes/graphql",
        "reference_url": "https://fastapi.tiangolo.com/how-to/graphql/",
    }
