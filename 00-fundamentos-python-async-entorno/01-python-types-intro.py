"""1/111 - Python Types Intro
https://fastapi.tiangolo.com/python-types/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/foundations/python-types-intro", tags=["Fundamentos de Python, async y entorno"])

from datetime import datetime
from pydantic import BaseModel
from typing import Annotated


class User(BaseModel):
    id: int
    name: str
    created_at: datetime | None = None
    friends: list[Annotated[int, "A list of user_id"]] = []

external_data = {
    "id": 1,
    "name": "John Doe",
    "created_at": datetime.now(),
    "friends": [3, 7, 65]
}

user1 = User(**external_data)

if __name__ == "__main__":
    print(user1.name)

@router.get("/")
async def read_lesson():
    return {
        "section": "Fundamentos de Python, async y entorno",
        "lesson": "Python Types Intro",
        "path": "/foundations/python-types-intro",
        "reference_url": "https://fastapi.tiangolo.com/python-types/",
    }
