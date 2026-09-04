"""42/111 - Simple OAuth2 with Password and Bearer
https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(
    prefix="/dependencies-security-middleware/simple-oauth2-with-password-and-bearer",
    tags=["Dependencias, seguridad básica y middleware"],
)


@router.get("/")
async def read_lesson():  # noqa
    return {
        "section": "Dependencias, seguridad básica y middleware",
        "lesson": "Simple OAuth2 with Password and Bearer",
        "path": "/dependencies-security-middleware/simple-oauth2-with-password-and-bearer",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/",
    }


"""
    ...

"""

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    },
    "bob": {
        "username": "bob",
        "full_name": "Bob Marley",
        "email": "bob@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    },
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def fake_hash_password(password: str) -> str:
    return "fakehashed" + password


@router.get("/token")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> dict[str, str]:
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    return {"access_token": user.username, "type": "Bearer"}
