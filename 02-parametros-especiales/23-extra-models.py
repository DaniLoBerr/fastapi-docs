"""23/111 - Extra Models
https://fastapi.tiangolo.com/tutorial/extra-models/
"""

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/special-params/extra-models",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():  # noqa: ANN201
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Extra Models",
        "path": "/special-params/extra-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/extra-models/",
    }


"""
    NOTES: EXTRA MODELS
    El objetivo de FastAPI es prevenir la duplicación de código,
    por lo que, cuando varios modelos Pydantic comparten información,
    lo más recomendable es crear un modelo base e ir creando
    diferentes modelos que hereden de él y que vayan añadiendo
    información para diferentes acciones.
"""


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hashed(raw_password: str) -> str:
    return "hashed! " + raw_password


def fake_save_user(user_in: UserIn) -> UserInDB:
    return UserInDB(
        **user_in.model_dump(), hashed_password=fake_password_hashed(user_in.password)
    )


@router.post("/save-user")
async def save_user(user_in: UserIn) -> UserOut:
    return fake_save_user(user_in)


"""
    NOTES: Union or AnyOf

    Cuando se declara una respuesta como una unión entre dos tipos,
    se debe colocar primero el más específico.

    Sintaxis:
    - Model1 | Model2: como anotación.
    - Union[Model1, Model2]: como argumento.
"""


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


@router.post("/save-items")
async def save_items(items: list[PlaneItem | CarItem]) -> list[PlaneItem | CarItem]:
    return items


"""
    NOTES: list of Items, arbitrary dict

    Se puede anotar o indicar en el response_model que la respuesta puede ser una lista
    de modelos Pydantic o un diccionarios de claves y valores cuando no sabemos exactamente
    cómo van a ser los campos (o claves en este caso) que vamos a recibir`.
"""


@router.post("/post-arbitrary-dict", response_model=dict[str, str])
async def post_arbitrary_dict(data: dict[str, str]) -> dict[str, str]:
    return data


"""
    RECAP:
    Use multiple Pydantic models and inherit freely for each case.
    You don't need to have a single data model per entity if that
    entity must be able to have different "states". The user "entity"
    is an example, with states that include password, password_hash,
    or no password.
"""
