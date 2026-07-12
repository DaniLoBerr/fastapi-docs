"""21/111 - Header Parameter Models
https://fastapi.tiangolo.com/tutorial/header-param-models/
"""

from typing import Annotated

from fastapi import APIRouter, Header
from pydantic import BaseModel

router = APIRouter(
    prefix="/special-params/header-parameter-models",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Header Parameter Models",
        "path": "/special-params/header-parameter-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/header-param-models/",
    }


# Pydantic Header Models

#   You can create a Pydantic model to declare a related group of headers you want to
#   receive in your path operation function.

#   You can also forbid the client sending extra headers

#   You can also disable the conversion of underscore to hyphens (Header(convert_underscores=False))


class CommonHeaders(BaseModel):
    # model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@router.get("/header-param-models")
async def get_headers(headers: Annotated[CommonHeaders, Header()]):
    return headers
