"""22/111 - Response Model - Return Type
https://fastapi.tiangolo.com/tutorial/response-model/
"""

from typing import Any

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/special-params/response-model-return-type",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():  # noqa: ANN201
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Response Model - Return Type",
        "path": "/special-params/response-model-return-type",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/response-model/",
    }


"""
    NOTES: Response Model - Return Type

    - Things that FastAPI does with the return type:
        - Validate returned data.
        - Add JSON Schema for the response.
        - Serialize the returned data to JSON using Pydantic.
        - Limit and Filter the output data.

    - response_model parameter
        - Return some data that it's not exactly what the type declares
        - Example: return a dict but declare it as a Pydantic model
        - response_model handle all the documentation, validation, and so.
        - Use 'Any' to prevent IDE to complain
        - response_model has priority over function return

    - Using different models for input and output data
        - Doing this + using inheritance, you can get the best of
        both worlds: type annotations with tooling support and
        data filtering.
        - It's also beneficial to have clean code, best practices, DRY, etc
"""


# Pydantic models
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = 10.2
    tags: list[str] | None = []


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@router.post("/post-item", response_model=Item)
async def post_item(item: Item) -> Any:  # noqa: ANN401
    return item


@router.get("/get-items", response_model=list[Item])
async def get_items() -> Any:  # noqa: ANN401
    return [
        Item(name="Foo", price=10.99),
        Item(name="Bar", price=5.99),
    ]


@router.post("/post-user")
async def post_user(user: UserIn) -> BaseUser:
    return user


"""
    NOTES: Other Return Type Annotations
    - Response and its sub-classes

    - Invalid Return Type Annotations
        - Si no devuelves un tipo de dato compatible con Pydantic
        (un objeto de base de datos o una unión con Response en vez
        de un dict o BaseModel), FastAPI intentará convertirlo a
        modelo Pydantic, no podrá y lanzará un error.
        - Para evitar esto, puedes utilizar un modelo Pydantic
        para la respuesta o desabilitar el modelo de respuesta
        utilizando 'response_model=None' cuando no quieras que
        FastAPI cree el equema a partir de la anotación.
"""


@router.get("/get-portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


"""
    NOTES: Response Model encoding parameters
    - You can omit data from the result using these parameters:
        - response_model_exclude_unset=True: only include data directly
        setted in the request and exclude the empty or default fields.
        - response_model_exclude_defaults=True: exclude the dafault
        values even if you set them
        - response_model_exclude_none=True

    - response_model_include and response model exclude
        - También puedes utilizar estos parámetros y pasarles un set
        de str con el nombre de los atributos que quieres
        incluir o excluir, aunque sigue siendo recomendado utilizar los
        parámetros anteriores FastAPI generará el JSON Schema de la app
        a partir del modelo completo, aunque luego en el endpoint se
        excluyan ciertos campos.
        - Si se te olvida utilizar un set y en su lugar utilizas una lista
        o una tupla, el código no se romperá y FastAPI convertirá el tipo
        de dato a set.

    - Using lists instead of sets

"""


@router.get("/exclude-unset", response_model_exclude_unset=True)
async def exclude_unset(item: Item) -> Item:
    return item


@router.get("/exclude-defaults", response_model_exclude_defaults=True)
async def exclude_defaults(item: Item) -> Item:
    return item


@router.get("/exclude-none", response_model_exclude_none=True)
async def exclude_none(item: Item) -> Item:
    return item


@router.get("/exclude-price", response_model_exclude={"price"})
async def exclude_price(item: Item) -> Item:
    return item
