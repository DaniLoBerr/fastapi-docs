"""27/111 - Request Files
https://fastapi.tiangolo.com/tutorial/request-files/
"""

from typing import Annotated

from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/forms-files-errors/request-files",
    tags=["Formularios, ficheros y manejo de errores"],
)


@router.get("/")
async def read_lesson():  # noqa: ANN201
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Request Files",
        "path": "/forms-files-errors/request-files",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-files/",
    }


"""
    NOTES: Request Files

    Files son enviados como "form data".

    - File:
        - Recibir archivos pequeños en la petición, con tipo "bytes"
    (se cargan en la memoria RAM).
        - File es una clase que hereda de Form (aunque no deja de
        ser una función que devuelve una clase especial).

    - UploadFile:
        - Recibir archivos más grandes, con tipo UploadFile.

    Características y ventajas de UploadFile:
        - Usa un archivo temporal 'spooled' (es decir, con almacenamiento
        en memoria y volcado en disco). Se cargan en la RAM hasta cierto
        tamaño, después pasa al disco duro.
        - Puedes obtener metadatos.
        - Trabajar de manera asíncrona (file-like interface).
        - Expone un objeto Python del tipo SpooledTemporaryFile, útil para
        trabajar con librerías que esperen recibir objetos de ese tipo.

    Atributos:
    - filename (str).
    - content-type (str).
    - file (SpooledTemporaryFile).

    Métodos async:
    - write(data). str o bytes.
    - read(size). int (bytes or chars of the file).
    - seek(offset). Goes to the byte position (int) in the file.
    - close(). Closes the file.

    Puedes llamar a los métodos de manera asíncrona,
        contents = await myfile.read()
    o síncrona,
        contents = myfile.file.read()

    ENCODING
    - HTML Form encoding = application/x-www-form-urlencoded.
    - File Form encoding = multipart/form-data
    - JSON encoding = application/json

    Tanto File como UploadFiles pueden ser opcionales,
    se les pueden añadir metadatos,
    y se pueden recibir varios archivos (en forma de lista).
"""


@router.post("/post-files")
async def post_files(
    files: Annotated[list[bytes], File(description="A file read as bytes")],
) -> dict[str, int]:
    return {"file_sizes": next(len(file) for file in files)}


@router.post("/post-upload-files")
async def post_upload_files(
    files: Annotated[list[UploadFile], File(description="A file read as UploadFile")],
) -> dict[str, list[str]]:
    return {"filenames": [file.filename for file in files]}
