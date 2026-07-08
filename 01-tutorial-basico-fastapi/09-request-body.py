"""9/111 - Request Body
https://fastapi.tiangolo.com/tutorial/body/
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/user-guide/request-body", tags=["Tutorial Básico de FastAPI"]
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Request Body",
        "path": "/user-guide/request-body",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body/",
    }


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    if q:
        return {"item_id": item_id, "item": item, "q": q}

    return {"item_id": item_id, "item": item}
