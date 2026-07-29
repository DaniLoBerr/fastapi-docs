"""31/111 - JSON Compatible Encoder
https://fastapi.tiangolo.com/tutorial/encoder/
"""

from datetime import datetime

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

router = APIRouter(
    prefix="/forms-files-errors/json-compatible-encoder",
    tags=["Formularios, ficheros y manejo de errores"],
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "JSON Compatible Encoder",
        "path": "/forms-files-errors/json-compatible-encoder",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/encoder/",
    }


"""
    JSON COMPATIBLE ENCODER:

    Esta función sirve para convertir un tipo de dato
    en otro que sea compatible con JSON.
    Por ejemplo, la documentación pone el ejemplo de
    cuando necesitas guardar un información en forma
    de JSON en una base de datos (en una tipo NoSQL) y
    tienes un modelo Pydantic o un diccionario con
    campos que no son compatibles con JSON (objetos
    datetime, un id tipo UUID, etc). Estos dos casos
    los convierte a str, por ejemplo. El modelo Pydantic
    lo convierte a dict.
"""


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


@router.post("/jsonable-encoder/post-item")
async def jsonable_encoder_post_item(item: Item) -> dict:
    return jsonable_encoder(item)
