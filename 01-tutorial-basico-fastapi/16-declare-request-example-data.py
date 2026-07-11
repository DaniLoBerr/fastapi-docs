"""16/111 - Declare Request Example Data
https://fastapi.tiangolo.com/tutorial/schema-extra-example/
"""

from typing import Annotated

from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/user-guide/declare-request-example-data",
    tags=["Tutorial Básico de FastAPI"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Declare Request Example Data",
        "path": "/user-guide/declare-request-example-data",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/schema-extra-example/",
    }


# WAYS TO Declare Request Example Data
# OpenAPI-specific (openapi_examples) vs JSON schema examples
#   json schema examples -> just a list of examples
#   openapi-specific -> dict with extra metadata


# 1 Extra JSON Schema data in Pydantic models
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Headphones", "price": 29.99},
                {
                    "name": "Laptop",
                    "description": "The good ol' laptop",
                    "price": 699.99,
                    "tax": 21.99,
                },
            ]
        }
    }


@router.post("/json-schema-examples-in-pydantic-model")
async def json_schema_examples_in_pydantic_model(item: Item):
    return item


# 2 Field additional arguments
class Item2(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


class User(BaseModel):
    name: str = Field(examples=["daniloberr"])


@router.post("/json-schema-examples-in-field-arguments")
async def json_schema_examples_in_field_arguments(user: User):
    return user


# 3 examples in JSON Schema - OpenAPI (Body, Path, Query...)
class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/json-schema-examples-in-body-arguments")
async def json_schema_examples_in_body_arguments(
    item: Annotated[
        Item3,
        Body(
            examples=[
                {"name": "Foo", "price": 35.4},
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            ]
        ),
    ],
):
    return item


# OpenAPI-specific
class Item4(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/openapi-examples")
async def openapi_examples(
    item: Annotated[
        Item4,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",  # .md syntax
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {"name": "Bar", "price": "35.4"},
                },
                "invalid": {
                    "summary": "An example of an invalid data",
                    "description": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
                "other": {
                    "summary": "An example from an external source",
                    "description": "This example is loaded from an external URL.",
                    "externalValue": "https://example.com/examples/item.json",
                },
            }  # type: ignore
        ),
    ],
):
    return item
