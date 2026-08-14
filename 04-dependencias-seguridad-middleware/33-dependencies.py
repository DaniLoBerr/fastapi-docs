"""33/111 - Dependencies
https://fastapi.tiangolo.com/tutorial/dependencies/
"""

from typing import Annotated, Any

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/dependencies-security-middleware/dependencies",
    tags=["Dependencias, seguridad básica y middleware"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Dependencies",
        "path": "/dependencies-security-middleware/dependencies",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/",
    }


"""
    DEPENDENCIAS

    - Las dependencias en FastAPI son funciones o recursos que otras
    funciones necesitar para funcionar.
    - La inyección de dependecias es el mecanismo que utiliza FastAPI para
    ejecutar esas dependecias y proporcionar su resultado a la función
    que las necesita cuando se ejecuta.

    First steps:
    1. Crear una función que represente la dependencia
    (Dependency/Dependable).
    2. Declarar la dependencia en la función que la necesita
    (the dependant), utilizando el decorador `Depends()`.
    3. Depends() solo recibe 1 único argumento y debe ser
    algo como una función (y solo la declaración, no la llamada
    a la función).
    4. Cuando la api reciba una petición, FastAPI ejecutará la
    función de dependencia con los parámetros correctos y pasará
    su resultado a la función que la necesita.

    Share Annoated dependencies:
    - Usando el "type alias" de Python, se puede declarar la
    dependencia en un solo lugar y luego reutilizarla en varias
    funciones, manteniendo todas las ventajas (código limpio,
    validación, documentación, etc.) de las dependencias.

    Async or not to async:
    - Las dependencias pueden ser funciones normales o funciones
    asíncronas. FastAPI se encargará de ejecutarlas correctamente
    según sea necesario.

    FastAPI plugins and compatibility:
    - FastAPI no necesita un sistema específico de plugins para
    integrar funcionalidades externas. Su sistema de Dependency
    Injection permite integrar fácilmente bases de datos,
    APIs externas, sistemas de autenticación, librerías y
    otros servicios mediante dependencias.
    - La dependencia actúa como puente entre FastAPI y un
    componente externo. FastAPI solo necesita saber cómo
    obtener ese componente; no necesita conocer los detalles
    de cómo funciona.
"""


async def common_params(q: str, skip: int = 0, limit: int = 10) -> dict[str, Any]:
    return {"q": q, "skip": skip, "limit": limit}


CommonDeps = Annotated[dict, Depends(common_params)]


@router.get("/get-users")
async def get_users(params: CommonDeps) -> dict:
    return params


@router.get("/get-items")
async def get_items(params: CommonDeps) -> dict:
    return params
