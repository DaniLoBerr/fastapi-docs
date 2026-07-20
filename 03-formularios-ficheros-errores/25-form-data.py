"""25/111 - Form Data
https://fastapi.tiangolo.com/tutorial/request-forms/
"""

from typing import Annotated

from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/forms-files-errors/form-data",
    tags=["Formularios, ficheros y manejo de errores"],
)


@router.get("/")
async def read_lesson():  # noqa: ANN201
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Form Data",
        "path": "/forms-files-errors/form-data",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-forms/",
    }


"""
    NOTES: Form Data

    Cuando quieres recibir datos a través de un formulario
    en vez de enformato JSON.

    - Password flow: Es una de las maneras en que la especificación
    OAuth2 puede ser usada y en ella se requiere enviar un
    username y un password exactamente con estos nombres en forma
    de campos de formulario.
    - Con Form puedes declarar las mismas configuraciones que con
    Body, Query, Path, Cookie...
    - Form es una clase que hereda de Body.
    - Si no declaras los parámetros como Form, serán declarados
    automáticamente como Query parameters.
    - HTML Form encoding = application/x-www-form-urlencoded.
    - File Form encoding = multipart/form-data
    - JSON encoding = application/json
    - No puedes recibir parámetros Body y Form en la misma request,
    como parte del protocolo HTTP.
"""


@router.post("/post-form-data")
async def post_form_data(
    username: Annotated[str, Form()], password: Annotated[str, Form()]
) -> dict[str, str]:
    return {"username": username, "password": password}
