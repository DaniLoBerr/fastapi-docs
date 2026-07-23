"""28/111 - Request Forms and Files
https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
"""

from typing import Annotated, Any

from fastapi import APIRouter, File, Form, UploadFile

router = APIRouter(
    prefix="/forms-files-errors/request-forms-and-files",
    tags=["Formularios, ficheros y manejo de errores"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Formularios, ficheros y manejo de errores",
        "lesson": "Request Forms and Files",
        "path": "/forms-files-errors/request-forms-and-files",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/request-forms-and-files/",
    }


"""
    NOTES: Requests with Forms and Files
    - When you want to receive data from a form, you can use Form.
    - When you want to receive files, you can use File.
    - You can use Form and File together in the same endpoint.
"""


@router.post("/post-files")
async def post_files(
    token: Annotated[str, Form()],
    file_a: Annotated[bytes, File()],
    file_b: Annotated[UploadFile, File()],
) -> dict[str, Any]:
    return {"token": token, "file_a": len(file_a), "file_b": file_b.filename}
