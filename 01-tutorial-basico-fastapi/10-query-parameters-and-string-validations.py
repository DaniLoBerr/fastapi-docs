"""10/111 - Query Parameters and String Validations
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
"""

from typing import Annotated

from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/user-guide/query-parameters-and-string-validations",
    tags=["Tutorial Básico de FastAPI"],
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Query Parameters and String Validations",
        "path": "/user-guide/query-parameters-and-string-validations",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/query-params-str-validations/",
    }


# Newer versions: Python 3.10+, FastAPI 0.95+ PREFERRED
@router.get("/items")
async def get_items(q: Annotated[str | None, Query(max_length=50)] = None):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        items.update({"q": q})

    return items


# Older versions: Python 3.10- Non-Annotated, FastAPI 0.95- NON-PREFERRED
@router.get("/items")
async def get_items(q: str | None = Query(default=None, max_length=50)):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        items.update({"q": q})

    return items
