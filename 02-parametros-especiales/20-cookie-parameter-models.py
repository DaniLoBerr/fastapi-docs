"""20/111 - Cookie Parameter Models
https://fastapi.tiangolo.com/tutorial/cookie-param-models/
"""

from typing import Annotated

from fastapi import APIRouter, Cookie
from pydantic import BaseModel

router = APIRouter(
    prefix="/special-params/cookie-parameter-models",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Cookie Parameter Models",
        "path": "/special-params/cookie-parameter-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/cookie-param-models/",
    }


# Pydantic Cookie Models

#   You can create a Pydantic model to declare a related group of cookies you want to
#   receive in your path operation function.

#   You can also forbid the client sending extra cookies


class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@router.get("/cookie-param-models")
async def get_cookies(cookies: Annotated[Cookies, Cookie()]):
    return cookies
