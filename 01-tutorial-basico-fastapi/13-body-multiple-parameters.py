"""13/111 - Body - Multiple Parameters
https://fastapi.tiangolo.com/tutorial/body-multiple-params/
"""

from typing import Annotated

from fastapi import APIRouter, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/user-guide/body-multiple-parameters", tags=["Tutorial Básico de FastAPI"]
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Body - Multiple Parameters",
        "path": "/user-guide/body-multiple-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-multiple-params/",
    }


class User(BaseModel):
    username: str
    full_name: str | None = None


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.put("/mix-path-query-multiple-extra-body/{item_id}")
async def mix_path_query_multiple_extra_body_request(
    *,
    item_id: Annotated[int, Path(title="The ID of the Item to get", gt=0, le=1000)],
    item: Item | None = None,
    user: User | None = None,
    extra_body: Annotated[str, Body()],
    q: str | None = None,
):
    results = {"item_id": item_id}
    if item:
        results.update({"item": item})
    if q:
        results.update({"q": q})
    if user:
        results.update({"user": user})
    if extra_body:
        results.update({"extra_body": extra_body})
    return results


# Embed
@router.put("/embed/{item_id}")
async def embed(
    *,
    item_id: Annotated[int, Path(title="The ID of the Item to get", gt=0, le=1000)],
    specific_item: Annotated[Item, Body(embed=True)],
):
    results = {"item_id": item_id, "specific_item": specific_item}
    return results
