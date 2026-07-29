"""30/111 - Path Operation Configuration
https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
"""

from enum import Enum

from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/forms-files-errors/path-operation-configuration",
    tags=["Formularios, ficheros y manejo de errores"],
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Path Operation Configuration",
        "path": "/forms-files-errors/path-operation-configuration",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/path-operation-configuration/",
    }


"""
    MANERAS DE CONFIGURAR EL PATH OPERATOR (El decorador):

    1. Response Status Code:

    Sirve para indicar el código HTTP que devolverá la ruta y
    para que quede documentado correctamente en OpenAPI.
"""


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@router.post("/path-status-code", status_code=status.HTTP_201_CREATED)
async def path_status_code(item: Item) -> Item:
    return item


"""
    2. Tags:

    Sirven para organizar y clasificar los endpoints en la
    documentación automática de FastAPI.
"""


@router.post("/tags/post-item", tags=["Items"])
async def tags_post_item(item: Item) -> Item:
    return item


@router.get("/tags/get-item", tags=["Items"])
async def tags_get_item() -> dict[str, int]:
    return {"item_id": 1}


@router.get("/tags/get-username", tags=["Users"])
async def tags_get_username() -> dict[str, str]:
    return {"username": "daniloberr"}


"""
    3. Tags with enums:

    Se pueden utilizar enums cuando hay varios
    tags y se quiere uno asegurar que se use la
    misma.
"""


class Tags(Enum):
    items = "Items"
    users = "Users"


@router.post("/enums/post-item", tags=[Tags.items])
async def enums_post_item(item: Item) -> Item:
    return item


@router.get("/enums/get-item", tags=[Tags.users])
async def enums_get_user() -> dict[str, str]:
    return {"user": "daniloberr"}


"""
    4. Summary and Description

    Sirven para poner un título corto y una explicación
    más larga a la ruta en la documentación automática de FastAPI.
"""


@router.post(
    "/summary-description/post-item",
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def summary_description(item: Item) -> Item:
    return item


"""
    5. Description for docstring

    Puedes escribir la descripción en el docstring del
    endpoint y tendrá la misma funcionalidad que el parámetro
    description. Puedes utilizar notación MarkDown.
"""


@router.post("/docstring/post-item", summary="Create an Item")
async def docstring_description(item: Item) -> Item:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


"""
    6. Response Description

    Esto es la decripción que se le da a la respuesta en el
    equema OpenAPI. Si no se especifica ninguna, FastAPI
    genera una automática. Por ejemplo, un respuesta 200
    se vería en OpenAPI como "Succesful response"
"""


@router.post(
    "/response-description/post-item",
    summary="Create an item",
    response_description="The created item",
)
async def response_description_post_item(item: Item) -> Item:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


"""
    7. Deprecate a Path Operation

    Para marcar un método como deprecado pero
    sin borrarlo del esquema.
"""


@router.get("/deprecate/get-item", tags=["Items"])
async def deprecate_get_item() -> dict[str, str | int]:
    return {"name": "Foo", "price": 42}


@router.get("/deprecate/get-user/", tags=["Users"])
async def deprecate_get_user() -> dict[str, str]:
    return {"username": "johndoe"}


@router.get("/deprecate/get-element", tags=["Items"], deprecated=True)
async def deprecate_get_element() -> dict[str, str]:
    return {"item_id": "Foo"}
