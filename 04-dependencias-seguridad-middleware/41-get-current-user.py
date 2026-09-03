"""41/111 - Get Current User
https://fastapi.tiangolo.com/tutorial/security/get-current-user/
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

router = APIRouter(
    prefix="/dependencies-security-middleware/get-current-user",
    tags=["Dependencias, seguridad básica y middleware"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Get Current User",
        "path": "/dependencies-security-middleware/get-current-user",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/get-current-user/",
    }


"""
    GET CURRENT USER

    Aquí la documentación explica cómo obtener la información
    del usuario a partir de un token de acceso que ya existe,
    es decir, a partir de un token que el usuario ya generó
    al loguearse con sus credenciales en una petición anterior.
    Esta lección no explica cómo se genera el token (eso se
    ve en la siguiente lección con OAuth2 y JWT), sino cómo
    se usa un token ya emitido para identificar al usuario.

    Cuando un usuario se loguea con sus credenciales,
    normalmente una app genera un token de acceso para
    autenticar al usuario las siguientes veces que
    acceda a la app sin tener que pedirle las
    credenciales cada vez.

    Entonces lo que ocurre es que en la request normalmente
    viene un header Authorization con un token del tipo
    Bearer, que la app decodifica para obtener la información
    del usuario y devolverla en la respuesta.

    Cabe también destacar 3 cosas:
    - El encadenamiento de dependencias: "get_current_user" depende
    a su vez de "oauth2_scheme" mediante Depends, formando un
    árbol de dependencias.
    - La reutilización de la dependencia "get_current_user": al ser
    una dependencia independiente, se puede inyectar en cualquier
    path operation sin repetir la lógica de extraer y decodificar
    el token.
    - La agnosticidad del dato que devuelve la dependencia: no está
    obligada a devolver un modelo User de Pydantic, podría devolver
    un dict, un str o un objeto de base de datos. Aquí se usa User
    para aprovechar el autocompletado y el chequeo de tipos del editor.
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def decode_access_token(token: str) -> User:
    return User(
        username=token + "fake_decode",
        email="example@email.com",
        full_name="Foo Bar",
        disabled=False,
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user = decode_access_token(token)
    return user


@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    return current_user
