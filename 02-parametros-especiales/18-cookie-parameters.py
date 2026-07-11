"""18/111 - Cookie Parameters
https://fastapi.tiangolo.com/tutorial/cookie-params/
"""

from typing import Annotated

from fastapi import APIRouter, Cookie

router = APIRouter(
    prefix="/special-params/cookie-parameters",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Cookie Parameters",
        "path": "/special-params/cookie-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/cookie-params/",
    }


# COOKIE PARAMETERS
@router.get("/cookie-params")
async def cookie_params(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


"""No se puede ejecutar el código en Swagger UI:

la interfaz de documentación interactiva (la UI en /docs) usa JavaScript
en el navegador para hacer las peticiones desde la página,
y por diseño los navegadores gestionan las cookies de forma limitada y
"silenciosa", de modo que esa UI no puede poner o enviar cookies
arbitrarias que hayas escrito en los campos de la documentación;
por eso aunque rellenes el formulario y pulses "Execute" la cookie no
llegará al servidor y la petición fallará como si no hubieras enviado
nada.
"""
