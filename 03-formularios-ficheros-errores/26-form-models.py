"""26/111 - Form Models
https://fastapi.tiangolo.com/tutorial/request-form-models/
"""

from typing import Annotated

from fastapi import APIRouter, Form
from pydantic import BaseModel

router = APIRouter(
    prefix="/forms-files-errors/form-models",
    tags=["Formularios, ficheros y manejo de errores"],
)


@router.get("/")
async def read_lesson():  # noqa: ANN201
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Form Models",
        "path": "/forms-files-errors/form-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-form-models/",
    }


"""
    NOTES: Form Models

    Puedes crear un modelo Pydantic con los datos
    que esperas recibir de un formulario.
    También puedes prohibir campos extras.
"""


class FormData(BaseModel):
    username: str
    password: str

    model_config = {"extra": "forbid"}


@router.post("/post-form-model")
async def post_form_model(data: Annotated[FormData, Form()]) -> FormData:
    return data
