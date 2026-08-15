"""36/111 - Dependencies in path operation decorators
https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException

router = APIRouter(
    prefix="/dependencies-security-middleware/dependencies-in-path-operation-decorators",
    tags=["Dependencias, seguridad básica y middleware"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Dependencies in path operation decorators",
        "path": "/dependencies-security-middleware/dependencies-in-path-operation-decorators",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/",
    }


"""
    DEPENDENCIES IN PATH OPERATION DECORATORS

    Se puede utilizar el parámetro "dependencies" en los decoradores
    de operaciones de ruta para declarar una lista dedependencias que
    se aplican a la operación de ruta.

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


async def verify_token(x_token: Annotated[str, Header()]) -> None:
    if x_token != "Super-secret-token":  # noqa
        raise HTTPException(status_code=400, detail="X-Token header not valid")


async def verify_key(x_key: Annotated[str, Header()]) -> str:
    if x_key != "Super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header not valid")
    return x_key


@router.get("/items", dependencies=[Depends(verify_token), Depends(verify_key)])
async def get_items() -> list[dict[str, str]]:
    return [{"item": "foo"}, {"item": "bar"}]
