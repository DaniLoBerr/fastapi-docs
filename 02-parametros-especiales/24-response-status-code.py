"""24/111 - Response Status Code
https://fastapi.tiangolo.com/tutorial/response-status-code/
"""

from fastapi import APIRouter, status

router = APIRouter(
    prefix="/special-params/response-status-code",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():  # noqa: ANN201
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Response Status Code",
        "path": "/special-params/response-status-code",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/response-status-code/",
    }


"""
    NOTES: Status Code

    En el parámetro status_code del decorador puedes indicar el
    código HTTP que quieres que devuelva la respuesta (también
    se documentará en el esquema de la app en OpenAPI).

    Valores:
    - El número directamente (200).
    - Un IntEnum de Python (HTTPStatus.OK).
    - Un fastapi.status, que es lo mismo que starlet.status
    (fastapi.status.HTTP_200_OK)

    - 100-199: Information.
    - 200-299: Success.
    - 300-399: Redirection.
    - 400-499: Client.
    - 500-599: Server.
"""


@router.post("/status-code", status_code=status.HTTP_201_CREATED)
async def status_code(name: str) -> dict[str, str]:
    return {"name": name}
