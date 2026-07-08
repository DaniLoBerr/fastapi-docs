"""10/111 - Query Parameters and String Validations
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
"""

from random import choice
from typing import Annotated

from fastapi import APIRouter, Query
from pydantic import AfterValidator

router = APIRouter(
    prefix="/user-guide/query-parameters-and-string-validations",
    tags=["Tutorial Básico de FastAPI"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Query Parameters and String Validations",
        "path": "/user-guide/query-parameters-and-string-validations",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/query-params-str-validations/",
    }


# CODE EXAMPLES:


# QUERY PARAMETER
@router.get("/items-query-parameter")
async def items_query_parameter(q: str | None = None):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        items.update({"q": q})
    return items


# ADITIONAL VALIDATION
#   Generic validations: alias, deprecated, description, title, exclude (include_in_schema)
#   Validation specific for strings: max_length, min_length, pattern


#   Newer versions: Python 3.10+, FastAPI 0.95+ PREFERRED
@router.get("/aditional-validation-new")
async def aditional_validation_new(
    q: Annotated[
        str | None,
        Query(
            alias="aditional-validation",
            deprecated=True,
            description="Example of Aditional Validation",
            max_length=50,
            min_length=3,
            pattern="^fixedquery$",
            title="Aditional Validation",
        ),
    ] = None,
    hidden: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        items.update({"q": q})

    if hidden:
        items.update({"hidden_query": hidden})

    return items


#   Older versions: Python 3.10- Non-Annotated, FastAPI 0.95- NON-PREFERRED
@router.get("/aditional-validation-old")
async def aditional_validation_old(
    q: str | None = Query(
        alias="aditional-validation",
        default=None,
        deprecated=True,
        description="Example of Aditional Validation",
        max_length=50,
        min_length=3,
        pattern="^fixedquery$",
        title="Aditional Validation",
    ),
    hidden: str | None = Query(default=None, include_in_schema=False),
):
    items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        items.update({"q": q})

    if hidden:
        items.update({"hidden_query": hidden})

    return items


# Custom Validation: AfterValidator, BeforeValidator, ...


# Optional? None or any other default value
# Required? Not adding default value. Can be None
# You can recieve a list of values like:
#   http://localhost:8000/items/?q=foo&q=bar
#   But you have to declare the parameter as Query:
@router.get("/aditional-validation-list")
async def aditional_validation_list(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items


# CUSTOM VALIDATION
#   AfterValidator
data: dict[str, str] = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@router.get("/custom-validation")
async def custom_after_validation(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = choice(list(data.items()))
    return {"id": id, "name": item}
