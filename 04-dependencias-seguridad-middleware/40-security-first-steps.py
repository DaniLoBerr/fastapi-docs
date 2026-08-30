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

    Documentación desde los docs. Autorizar, debuguear,
    utilizar por el front.
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items")
async def get_items(token: Annotated[str, Depends(oauth2_scheme)]):  # noqa
    return {"token": token}


"""
    THE PASSWORD FLOW


"""
