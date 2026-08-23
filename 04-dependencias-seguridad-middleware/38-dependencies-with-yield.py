"""38/111 - Dependencies with yield
https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path

router = APIRouter(
    prefix="/dependencies-security-middleware/dependencies-with-yield",
    tags=["Dependencias, seguridad básica y middleware"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Dependencies with yield",
        "path": "/dependencies-security-middleware/dependencies-with-yield",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/",
    }


"""
    DEPENDENCIES WITH YIELD

    Cuando se utiliza yield en una dependencia, FastAPI ejecutará
    el código antes del yield cuando se llame a la dependencia y
    luego ejecutará el código después del yield cuando la solicitud
    haya terminado.
"""

"""
    1. Dependencia de base de datos con yield.
    2. Y usando try/catch/finally.
"""


async def get_db():  # noqa
    # Obtienes la sesión de la BD
    db = DBSession()  # type: ignore # noqa
    try:
        # La envías al endpoint
        yield db
    finally:
        # Pase lo que pase, se cierra la sesión después de
        # que se haya utilizado en el endpoint o haya ocurrido
        # una excepción
        db.close()


"""
    3. Sub-dependencias usando yield

    Las subdependencias pueden usar tanto yield
    como return y FastAPI se encargará de cerrar
    los recursos en el orden correcto gracias a
    los context managers de Python.

        CREACIÓN
            ↓
            A
            ↓
            B
            ↓
            C
            ↓
        ENDPOINT
            ↓
        LIMPIEZA
            ↓
            C
            ↓
            B
            ↓
            A
"""


async def get_db():  # noqa: ANN201, F811
    db = create_db_session()  # type: ignore  # noqa: F821

    try:
        yield db
    finally:
        db.close()


async def get_repository(  # noqa: ANN201
    db: Annotated[DBSession, Depends(get_db)],  # type: ignore  # noqa: F821
):
    repository = Repository(db)  # type: ignore  # noqa: F821

    try:
        yield repository
    finally:
        repository.close()


"""
    4. Dependencias con yield y HTTPException

    Dependencies with yield pueden capturar excepciones
    producidas durante la ejecución del endpoint después
    del yield. Esto permite que la dependencia reaccione
    ante ellas o las transforme, por ejemplo, en una
    HTTPException. Es una técnica avanzada y poco habitual;
    si el propio endpoint sabe que debe devolver un error HTTP,
    normalmente puede lanzar directamente HTTPException.
"""

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}


class OwnerError(Exception):
    pass


async def get_username():  # noqa: ANN201, F811, RUF100
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")  # noqa: B904


@router.get("/items/{item_id}")
async def get_item(  # noqa: ANN201
    item_id: Annotated[str, Path()], username: Annotated[str, Depends(get_username)]
):  # type: ignore
    if item_id not in data:
        raise HTTPException(status_code=400, detail="Item not found")
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item


"""
    5. Dependecies qith yield and except

    Cuando lanzas un error en un endpoint, lo capturas en la
    dependencia y no lo vuelves a lanzar, la excepción se
    consume y FastAPI lo que devuelve por defecto es un error 500,
    pero sin información relevante para los logs y el debuggin.
"""


class InternalError(Exception):
    pass


async def get_username_print():  # noqa: ANN201
    try:
        yield "Rick"
    except InternalError:
        print("Oops, we didn't raise again, Britney 😱")


@router.get("/items_print/{item_id}")
async def get_item_print(  # noqa: ANN201
    item_id: Annotated[str, Path()],
    username: Annotated[str, Depends(get_username_print)],
):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only aplumbus here"
        )
    return item_id


"""
    5.1 Always raise in Dependencies with yield and except

    Puedes transformar la excepción en otra o simplemente
    printear/loguear información sobre el error y después
    volver a lanzar la misma excepción utilizando solo
    la palabra "raise".
"""


async def get_username_print():  # noqa: ANN201
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise


@router.get("/items_raise/{item_id}")
async def get_item_raise(  # noqa: ANN201
    item_id: Annotated[str, Path()],
    username: Annotated[str, Depends(get_username_print)],
):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only aplumbus here"
        )
    return item_id
