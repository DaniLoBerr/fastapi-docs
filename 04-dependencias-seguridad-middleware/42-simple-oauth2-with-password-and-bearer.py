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
    SIMPLE OAuth2 WITH PASSWORD AND BEARER

    En esta lección se aprende a utilizar el flow password de
    la especificación OAuth2: Los datos del cliente se deben
    enviar como datos de formulario con los campos
    username y password.

    Lo que cierra esta lección es el siguiente flujo:
        - Login (una vez): credenciales → token.
        - Petición (siempre después): token → usuario.

        FLUJO 1: LOGIN (obtener el "token")
        ════════════════════════════════════

        Cliente                    GET /token                  fake_users_db
        |                            |                              |
        |--- username, password ---->|                              |
        |                            |--- .get(username) ---------->|
        |                            |<--- user_dict / None ---------|
        |                            |
        |                     [user_dict is None?]
        |                            |--- sí --> 400 Incorrect username or password
        |                            |
        |                     fake_hash_password(password)
        |                            |
        |                     [hash != hashed_password?]
        |                            |--- sí --> 400 Incorrect username or password
        |                            |
        |<--- {"access_token": username, "type": "Bearer"} ----------|


        FLUJO 2: ACCESO A RUTA PROTEGIDA
        ═════════════════════════════════

        Cliente         GET /users/me       get_current_active_user   get_current_user
        |                   |                       |                      |
        |-- Authorization: Bearer <token> --------->|                      |
        |                   |          Depends() -->|                      |
        |                   |                       |---- Depends() ------>|
        |                   |                       |                      |
        |                   |                       |            oauth2_scheme extrae
        |                   |                       |            el token del header
        |                   |                       |                      |
        |                   |                       |            fake_decode_token(token)
        |                   |                       |              = get_user(db, token)
        |                   |                       |                      |
        |                   |                       |          [user is None?]
        |                   |                       |<-- sí -- 401 Not authenticated
        |                   |                       |          (header WWW-Authenticate: Bearer)
        |                   |                       |                      |
        |                   |                       |<---- User -----------|
        |                   |                       |
        |                   |            [user.disabled?]
        |                   |<-- sí -- 400 Inactive user
        |                   |
        |                   |<---- User -------------|
        |<--- User (JSON) --|



    FORM DATA:
    Para obtener los datos de los campos del formulario con FastAPI,
    utilizamos la clase OAuth2PasswordRequestForm. Esta clase delcara
    los siguientes campos:
    - Username (obligatorio): identificador del usuario. Ejemplo: "johndoe".
    - Password (obligatorio): contraseña en texto plano. Ejemplo: "Abc1234!!".
    - grant_type (opcional, pero restringido por Form(pattern="password)):
        Identifica que flujo de OAuth2 se está utilizando en esta petición
        al endpoint /token. Nosotros estamos utilizando el flow password en el
        ejemplo del código pero se podrían utilizar otros. Ejemplos: 'authorization_code',
        'client_credentials', 'refresh_token'.
    - Scope (opcional):
        Un string con el que el cliente pide permisos concretoa al token. Pueden
        venir varios 'scopes'. Ejemplo: 'items:read items:write'.
    - client_id (opcional):
        Identifica a la aplicación cliente en caso de que el servidor de autorización
        registre clientes distintos. Ejemplo: "mobile-client-key".
    - client_secret (opcional):
        String para autenticar a la aplicación cliente. Ejemplo: "s3cr3t-client-key".


    SCOPE:
    Es importante aclarar que este campo se llama 'scope' en el formulario de
    la petición HTTP y es un string pero se llama 'scopes' en el diccionario de Python
    que genera FastAPI y es una lista de strings con los diferentes valores
    separados.

    LOGIN RESPONSE:
    La respuesta del login, por definición de la especificación, debe tener
    la siguiente estructura:
        {"access_token": "token", "type": "Bearer"}

    HEADER 'WWW-Authenticate':
    Por obligatoriedad esta vez de la especificación HTTP, cuando un servidor responde
    con un 401 Unauthorized, la respuesta debe incluir este header para indicar al cliente
    cómo debe autenticarse. En este caso, como es de tipo 'Bearer', se incluye este valor.

"""

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fake_hashed_Abc1234!!",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fake_hashed_Abc1234!!",
        "disabled": True,
    },
    "bob": {
        "username": "bob",
        "full_name": "Bob Marley",
        "email": "bob@example.com",
        "hashed_password": "fake_hashed_Abc1234!!",
        "disabled": False,
    },
    "daniloberr": {
        "username": "daniloberr",
        "full_name": "Daniel López Berrocal",
        "email": "daniellopez@yopmail.com",
        "hashed_password": "fake_hashed_Abc1234!!",
        "disabled": False,
    },
}

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/dependencies-security-middleware/simple-oauth2-with-password-and-bearer/token"
)


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def fake_decode_token(token: str) -> User:
    # No hay decodificación aquí. Esto se añade en la lección siguiente
    return get_user(fake_users_db, token)


def fake_hash_password(password: str) -> str:
    return "fake_hashed_" + password


def get_user(db: dict, username: str) -> UserInDB | None:
    return UserInDB(**db[username]) if username in db else None


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_active_user(
    user: Annotated[User, Depends(get_current_user)],
) -> User:
    if user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


@router.get("/users/me")
async def read_users_me(user: Annotated[str, Depends(get_current_active_user)]) -> User:
    return user


@router.post("/token")
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
