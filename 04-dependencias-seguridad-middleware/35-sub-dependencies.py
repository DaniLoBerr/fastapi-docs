"""35/111 - Sub-dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
"""

from typing import Annotated

from fastapi import APIRouter, Cookie, Depends

router = APIRouter(
    prefix="/dependencies-security-middleware/sub-dependencies",
    tags=["Dependencias, seguridad básica y middleware"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Sub-dependencies",
        "path": "/dependencies-security-middleware/sub-dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/",
    }


"""
    SUB-DEPENDENCIES
    ----------------

    Dependencias que tienen otras dependencias como parámetros.

    1. First dependency: Dependable
    2. Second dependency: Dependable and Dependant

    Por defecto, FastAPI ejecuta una dependencia como máximo una
    vez por request y reutiliza su resultado mediante una caché.
    use_cache=False desactiva este comportamiento para esa dependencia:

    async def needy_dependency(fresh_value: Annotated[str, Depends(get_value, use_cache=False)]):
        return {"fresh_value": fresh_value}
"""


async def query_extractor(q: str | None = None) -> str | None:
    return q


async def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_q: Annotated[str | None, Cookie()] = None,
) -> str | None:
    if not q:
        return last_q
    return q


@router.get("/get-query-or-cookie")
async def print_query_or_cookie(
    q_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
) -> dict:
    return {"query_or_cookie": q_or_default}
