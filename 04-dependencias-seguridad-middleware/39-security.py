"""39/111 - Security
https://fastapi.tiangolo.com/tutorial/security/
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/dependencies-security-middleware/security",
    tags=["Dependencias, seguridad básica y middleware"],
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Security",
        "path": "/dependencies-security-middleware/security",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/",
    }


"""
    SECURITY

    Conceptos:
    - Autenticación -> Validarte con tus datos en la aplicación.
    - Autorización -> Tener permisos para acceder a ciertos
    recursos de la aplicación.

    Esquemas de seguridad:
    - OAuth1 vs OAuth 2:
        - Ambos son estándares de seguridad que definen diferentes
        formas de gestionar la autenticación y autorización
        en una aplicación.
        - OAuth1 es un estándar más antiguo y complejo e incluye
        especificaciones sobre cómo encriptar la información.
        - OAuth2 es un estándar moderno que espera que la
        aplicación ya venga cifrada con HTTPS. Incluye
        la manera de autenticarse utilizado a terceros, como
        Google, GitHub, Facebook, etc.
    - OpenID vs OpenID Connect:
        - OpenID Connect es otro estándar basado en OAuth2
        utilizado por ejemplo por Google
        - OpenID es otra especificación pero que no está
        basada en OAuth2.
    - OpenAPI:
        - Es una especificación abierta y pensada para la
        implementación de APIs, y en la que está basada FastAPI.
        - Es la que permite que FastAPI tenga la documentación
        automática, generación del código, etc.
        - Con OpenAPI, se pueden definir los siguientes
        esquemas de seguridad:
            - apikey: Una clave que puede venir mediante
            un parámetro query, una cookie, o el header.
            - http: Sistemas de autenticación basados
            en http.
                - Basic HTTP.
                - Bearer Token: Un header "Authorization" que incluye
                el valor "Bearer" más un token.
            - oauth2: Diferentes "flows" para manejar la seguridad
            de la aplicación:
                - password.
                - implicit.
                - clientCredentials.
                - authorizationCode.
            - openIdconnect: Define como descubrir datos de
            autenticación OAuth2 de manera automática.

    FastAPI utilities:
    - En fastapi.security se pueden encontrar diferentes
    herramientas para implementar estos mecanismos de
    seguridad.
"""
