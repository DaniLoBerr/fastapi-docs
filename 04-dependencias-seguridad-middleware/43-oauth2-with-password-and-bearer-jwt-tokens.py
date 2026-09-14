"""43/111 - OAuth2 with Password (and hashing), Bearer with JWT tokens
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/dependencies-security-middleware/oauth2-with-password-and-bearer-jwt-tokens",
    tags=["Dependencias, seguridad básica y middleware"],
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "OAuth2 with Password (and hashing), Bearer with JWT tokens",
        "path": "/dependencies-security-middleware/oauth2-with-password-and-bearer-jwt-tokens",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/",
    }


"""
    OAuth2 with Password (and hashing), Bearer with JWT tokens

    En esta lección se completan las dos piezas que quedaron simuladas
    en las lecciones anteriores y que son necesarias para implementar
    la seguridad de nuestra API de forma correcta:
    - Cómo hashear las contraseñas de los usuarios para almacenarlas
    de forma segura.
    - Cómo autenticar al usuario en las siguientes peticiones HTTP,
    tras el login, utilizando un token JWT firmado.


    JWT (JSON Web Tokens)

    Es un estándar para codificar un objeto JSON en un string sin
    espacios. Ese string no está encriptado (cualquiera puede recuperar
    la información contenida en él) pero sí está firmado, lo que hace que
    puedas comprobar si el token que recibes ha sido emitido por tí mismo o
    si ha sido modificado. Por eso no se debe incluir información sensible en
    el token. Se le puede añadir una fecha de expiración.
    Para generar y verificar JWTs en Python se puede utilizar la librería PyJWT


    PASSWORD HASHING

    Hashear una contraseña significa convertirla en un string que que no pueda
    ser descifrado. Una misma contraseña debe de producir siempre el mismo hash.
    El hash debe de tener siempre un tamaño fijo. Cualquier mínimo cambio en el
    contenido que se hashea debe de producir un resultado diferente.
    Este procedimiento se utiliza para proteger la contraseña de los usuarios.
    Hoy en día el algoritmo de hash recomendado es Argon2.
    Para manejar hashes de contraseñas en Python se puede utilizar la librería
    pwdlib. Además, esta librería hace que se puedan compartir datos entre
    aplicaciones escritas en FastAPI, Django o Flask.
"""
