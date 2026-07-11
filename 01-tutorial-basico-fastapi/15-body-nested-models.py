"""15/111 - Body - Nested Models
https://fastapi.tiangolo.com/tutorial/body-nested-models/
"""

from typing import Annotated

from fastapi import APIRouter, Body
from pydantic import BaseModel, HttpUrl

router = APIRouter(
    prefix="/user-guide/body-nested-models", tags=["Tutorial Básico de FastAPI"]
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Body - Nested Models",
        "path": "/user-guide/body-nested-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-nested-models/",
    }


# Set types, Nested and deeply nested sub-models, special types


class Image(BaseModel):
    name: str
    url: HttpUrl  # Special type


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    img: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@router.post("/nested-models")
async def nested_models(offer: Annotated[Offer, Body(embed=True)]):
    return offer


# Bodies of pure lists
@router.post("/pure-lists")
async def pure_lists(images: list[Image]):
    return images


# Bodies of arbitrary dicts
#   Pydantic models = campos fijos, dict = campos variables
@router.post("/arbitrary-dicts")
async def arbitrar_dicts(some_dicts: dict[int, str]):
    return some_dicts
