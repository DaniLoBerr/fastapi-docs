"""19/111 - Header Parameters
https://fastapi.tiangolo.com/tutorial/header-params/
"""

from typing import Annotated

from fastapi import APIRouter, Header

router = APIRouter(
    prefix="/special-params/header-parameters",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Header Parameters",
        "path": "/special-params/header-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/header-params/",
    }


# HEADER PARAMETERS
@router.get("/headers")
async def headers(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


# Possibility of disable underscore conversion: Header(convert_underscores=False)
@router.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}


# Duplicate Headers
#   Receiving duplicate headers (several values of the same header) = list of strings
@router.get("/duplicate-headers")
async def duplicate_headers(x_token: Annotated[list[str], Header()]):
    return {"X-Token values": x_token}
