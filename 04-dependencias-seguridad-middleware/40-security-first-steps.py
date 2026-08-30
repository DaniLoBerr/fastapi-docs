"""40/111 - Security - First Steps
https://fastapi.tiangolo.com/tutorial/security/first-steps/
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/dependencies-security-middleware/security-first-steps",
    tags=["Dependencias, seguridad básica y middleware"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Security - First Steps",
        "path": "/dependencies-security-middleware/security-first-steps",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/first-steps/",
    }


"""
    SECURITY - FIRST STEPS

    Esta es una de las formas en las que nuestra API puede recibir
    un token de autenticación de forma estandarizada.

    La documentación interactiva de FastAPI es muy útil para probar,
    autorizar y depurar nuestra API, además de facilitar su uso
    por parte del frontend.
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items")
async def get_items(token: Annotated[str, Depends(oauth2_scheme)]):  # noqa
    return {"token": token}


"""
    THE PASSWORD FLOW

    El Password Flow es una de las formas definidas por OAuth2
    para gestionar la autenticación.

    OAuth2 permite separar la aplicación que proporciona los recursos
    (nuestra API) del proceso encargado de autenticar al usuario.

    Proceso:
    - El usuario introduce su username y password en el frontend.
    - El frontend envía estas credenciales a la ruta relativa
    definida por el parámetro "tokenUrl".
    - La API comprueba las credenciales y, si son correctas,
    devuelve un token.    THE PASSWORD FLOW

    El password flow es una de las maneras definidas en OAuth2
    para gestionar el tema de la seguridad.

    OAuth2 fue diseñado para que el backend o la api de una aplicación
    fueran independientes del servidor que autentica al usuario.
    En este caso la aplicación maneja la api y la autenticación.

    Proceso:
    - Cuando un usuario envía el username y el password desde el
    front, estos datos se envían a la ruta definida por el parámetro
    "tokenUrl".
    - La API chequea estos datos y, si son correctos,
    responde con un token.
    - El front almacena el token y lo utiliza para autenticar al
    usuario cada vez que este vuelve a intentar obtener
    otros datos de la API. El front envía el token como
    header "Authorization" con el esquema "Bearer + token".

    Lo que hacemos con el código anterior es que OAuth2PasswordBearer
    extraiga el Bearer token de la petición y que esta se pase como
    dependencia al endpoint
    - El frontend utiliza ese token en las siguientes peticiones
    a la API.
    - El token se envía en el header "Authorization" utilizando
    el esquema "Bearer":
        Authorization: Bearer <token>

    Lo que hacemos con el código anterior es utilizar
    OAuth2PasswordBearer como una dependencia para que FastAPI
    extraiga el Bearer token del header "Authorization" y nos lo
    entregue como el parámetro "token" del endpoint.

    IMPORTANTE:
        OAuth2PasswordBearer no valida ni autentica el token.
        Simplemente lo extrae de la petición.
"""
