"""14/111 - Body - Fields
https://fastapi.tiangolo.com/tutorial/body-fields/
"""

from typing import Annotated

from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/user-guide/body-fields", tags=["Tutorial Básico de FastAPI"]
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Body - Fields",
        "path": "/user-guide/body-fields",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-fields/",
    }


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        max_length=300,
        title="The description ot the item",
    )
    price: float = Field(
        description="The price must be greater than zero",
        gt=0,
    )
    tax: float | None = None


@router.put("/body-fields/{item_id}")
async def body_fields(item_id: int, item: Annotated[Item, Body(embed=True)]):
    return {"item_id": item_id, "item": item}
