"""32/111 - Body - Updates
https://fastapi.tiangolo.com/tutorial/body-updates/
"""

from datetime import datetime

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

router = APIRouter(
    prefix="/forms-files-errors/body-updates",
    tags=["Formularios, ficheros y manejo de errores"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Body - Updates",
        "path": "/forms-files-errors/body-updates",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/body-updates/",
    }


"""
    BODY - UPDATES

    - PUT y PATCH:
        Estos verbos HTTP se utilizan para sustituir la información
        de un determinado recurso de tu aplicación.

        - PUT se utiliza para sustituir el recurso completo, y los datos no
        indicados en la petición, quedarán vacíos o con su valor por defecto.

        - PATCH se utiliza para sustituir uno o varios campos concretos
        del recurso.

    Para realizar actualizaciones parciales es muy útil el
    parámetro 'exclude_unset' del método de Pydantic '.model_dump(),
    el cual convierte a dict los datos de un objeto de un modelo
    Pydantic excluyendo los datos que no han sido especificados en
    la petición.

    También, el modelo Pydantic tiene el método '.model_copy()', con el
    cual se puede hacer una copia de un objeto de un modelo Pydantic y,
    a través del parámetro 'update', pasarle un dict con el que
    modificar los campos del mismo.

    Cabe destacar aquí que para que todo esto funcione, el modelo
    Pydantic que va a recibir la información parcial debe de tener
    los campos que no va a recibir como opcionales. La documentación
    sugiere crear varios modelos Pydantic para diferentes acciones,
    es decir, un modelo campos obligatorios para la creación de la
    entrada en la base de datos por primera vez, y
    luego un modelo con campos opcionales para las actualizaciones.
"""


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    date: datetime


class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float | None = None
    date: datetime | None = None


items: dict[str, dict] = {}


@router.get("/body-updates-get", response_model=dict[str, dict])
async def body_updates_get() -> dict[str, dict]:
    return items


@router.post(
    "/body-updates-post/{item_id}",
    response_model=ItemCreate,
    status_code=status.HTTP_201_CREATED,
)
async def body_updates_post(item_id: str, item: ItemCreate) -> ItemCreate:
    item_to_store = jsonable_encoder(item)
    items[item_id] = item_to_store
    return item


@router.put("/body-updates-put/{item_id}", response_model=ItemCreate)
async def body_updates_put(item_id: str, item: ItemCreate) -> ItemCreate:
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )

    item_to_store = jsonable_encoder(item)
    items[item_id] = item_to_store
    return item


@router.patch("/body-updates-patch/{item_id}", response_model=ItemCreate)
async def body_updates_patch(item_id: str, item: ItemUpdate) -> ItemCreate:
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    stored_item_data = items[item_id]
    stored_item_model = ItemCreate(**stored_item_data)
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
