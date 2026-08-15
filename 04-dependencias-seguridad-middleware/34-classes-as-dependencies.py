"""34/111 - Classes as Dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/
"""

from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/dependencies-security-middleware/classes-as-dependencies",
    tags=["Dependencias, seguridad básica y middleware"],
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Classes as Dependencies",
        "path": "/dependencies-security-middleware/classes-as-dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/",
    }


"""
    DEPENDENCIAS (Declaradas como Clases)

    Funcionan de la misma manera pero añaden mejor soporte
    del IDE (autocompletado).


    Annotatted shortcut:

    Cuando la dependencia es específicamente una clase que
    FastAPI llamará para crear una instancia de la clase misma
    existe el siguiente atajo:
    - commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
    - commons: Annotated[CommonQueryParams, Depends()]
"""


class CommonParamsDep:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 10):  # noqa
        self.q = q
        self.skip = skip
        self.limit = limit


items: list[dict[str, str]] = [{"item1": "foo"}, {"item2": "bar"}, {"item3": "baz"}]


@router.get("/get-items")
async def get_items(params: Annotated[CommonParamsDep, Depends()]) -> dict:
    response = {}
    if params.q:
        response.update({"q": params.q})
    filtered_items = items[params.skip : params.skip + params.limit]
    response.update({"items": filtered_items})
    return response
