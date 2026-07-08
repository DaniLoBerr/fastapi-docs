"""11/111 - Path Parameters and Numeric Validations
https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
"""

from random import choice
from typing import Annotated

from fastapi import APIRouter, Path, Query
from pydantic import AfterValidator

router = APIRouter(
    prefix="/user-guide/path-parameters-and-numeric-validations",
    tags=["Tutorial Básico de FastAPI"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Path Parameters and Numeric Validations",
        "path": "/user-guide/path-parameters-and-numeric-validations",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/",
    }


# CODE EXAMPLES


# PATH PARAMETERS
@router.get("/items-path-parameter/{item_id}")
async def items_path_parameter(item_id: str | None):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if item_id:
        items.update({"q": item_id})
    return items


# ADITIONAL VALIDATION
#   Generic validations: alias, deprecated, description, title, exclude (include_in_schema)
#   Validation specific for strings: max_length, min_length, pattern


#   Newer versions: Python 3.10+, FastAPI 0.95+ PREFERRED
@router.get("/aditional-validation-new/{p}/{hidden}")
async def aditional_validation_new(
    p: Annotated[
        str | None,
        Path(
            deprecated=True,
            description="Example of Aditional Validation",
            max_length=50,
            min_length=3,
            pattern="^fixedquery$",
            title="Aditional Validation",
        ),
    ],
    hidden: Annotated[str | None, Path(include_in_schema=False)],
):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if p:
        items.update({"p": p})

    if hidden:
        items.update({"hidden_query": hidden})

    return items


#   Older versions: Python 3.10- Non-Annotated, FastAPI 0.95- NON-PREFERRED
@router.get("/aditional-validation-old/{p}/{hidden}")
async def aditional_validation_old(
    p: str | None = Path(
        deprecated=True,
        description="Example of Aditional Validation",
        max_length=50,
        min_length=3,
        pattern="^fixedquery$",
        title="Aditional Validation",
    ),
    hidden: str | None = Path(include_in_schema=False),
):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if p:
        items.update({"p": p})

    if hidden:
        items.update({"hidden_query": hidden})

    return items


# OTRAS COSAS A TENER EN CUENTA
#   En Python, primero van los parámetros “normales” y después los que tienen = con un valor por defecto.
#   Si quieres mezclar eso en FastAPI sin pelearte con Python, usa Annotated,
#   o pon los parámetros sin valor por defecto antes, o usa *.
@router.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# NUMBER VALIDATIONS: ge, gt, le, lt
@router.get("/number-validations/{id}")
async def number_validation_int(id: Annotated[float, Path(gt=10, lt=11)]):
    return {"id": id}
