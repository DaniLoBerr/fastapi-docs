"""37/111 - Global Dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException


async def validate_token(x_token: Annotated[str, Header()]) -> None:
    if not x_token == "fake-super-secret-token":  # noqa
        raise HTTPException(status_code=400, detail="Invalid validation token")


async def validate_key(x_key: Annotated[str, Header()]) -> str:
    if not x_key == "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="Invalid Secret Key")
    return x_key


router = APIRouter(
    prefix="/dependencies-security-middleware/global-dependencies",
    tags=["Dependencias, seguridad básica y middleware"],
    dependencies=[Depends(validate_token), Depends(validate_key)],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Global Dependencies",
        "path": "/dependencies-security-middleware/global-dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/",
    }


"""
    GLOBAL DEPENDENCIES

    Se puede utilizar el parámetro "dependencies" en la propia
    aplicación FastAPI para declarar una lista de dependencias que
    se aplican a todas las operaciones de ruta.

    La dependencia se ejecutará antes de la operación de ruta y puede
    no devolver ningún valor, o devolverlo pero no afectar la respuesta.
    Si la dependencia lanza una excepción, la operación de ruta no se ejecutará.

    Además ayuda a que, si la dependencia no devuelve ningún valor y el
    supuesto parámetro de la operación de ruta no se utiliza,
    puede evitar malentendidos sobre si la dependencia se utiliza
    o no en la operación de ruta.

    También ayuda a reutilizar dependencias que si queremos que
    devuelvan valores en otras operaciones de ruta pero no
    en esta en particular.
"""


# app = FastAPI(dependencies=[Depends(validate_token), Depends(validate_key)])


@router.get("/items")
async def get_items() -> list:
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@router.get("/users")
async def get_users() -> list:
    return [{"username": "Rick"}, {"username": "Morty"}]
