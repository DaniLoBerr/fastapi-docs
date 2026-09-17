"""43/111 - OAuth2 with Password (and hashing), Bearer with JWT tokens
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
"""

from fastapi import APIRouter
from pwdlib import PasswordHash
from pydantic import BaseModel

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


    HASH AND VERIFY PASSWORDS

    pwdlib.PasswordHash.recommended() es un método de clase que devuelve
    una instancia ya configurada con el algoritmo de hashing recomendado
    por la librería Argon2 y sus parámetros de coste seguros, y que
    utilizaremos para hashear y verificar contraseñas.
    Para trabajar con sistemas más antiguos, es recomendado passlib. Pero
    se lo que se puede hacer es leer y verificar hashes antiguos con passlib
    y generar nuevos con pwdlib.
    Para evitar un ataque de temporización, lo que se hace es, cuando el
    usuario no existe, se verifica igualmente contra un hash de mentira
    (DUMMY_HASH) para gastar el mismo tiempo que si si existeiese.


    HANDLE JWT TOKENS

    Antes de nada, mencionar que la SECRET_KEY no se puede guardar en el
    código porque hace que quien la tenga pueda emitir tokens válidos.
    Normalmente se guarda en un archivo .env (variables de entorno).
    Aquí lo dejamos en el código porque es una lección meramente
    educativa. En un proyecto real quedaría así:


        from pydantic_settings import BaseSettings


        class Settings(BaseSettings):
            secret_key: str
            algorithm: str = "HS256"
            access_token_expire_minutes: int = 30

            model_config = {"env_file": ".env"}


        settings = Settings()


    Si cambiáramos la SECRET_KEY, automáticamente todos los tokens
    emitidos antes dejan de validar de golpe porque sus firmas
    ya no se pueden reproducir.
"""


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}


password_hash = PasswordHash.recommended()
DUMMY_HASH = password_hash.hash("dummypassword")
SECRET_KEY = "e79f07760e3ff8b1ded65074a75689f9e8740c0414aba91ad87faa2584189e45"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


# Create a utility function to hash a password coming from the user.
def get_password_hash(password: str) -> str:
    return password_hash.hash(password)


# And another utility to verify if a received password matches the hash stored.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


# And another one to authenticate and return a user.
def get_user(db: dict, username: str) -> UserInDB:
    return UserInDB(**db[username]) if username in db else None


def authenticate_user(db: dict, username: str, password: str) -> User | bool:
    user = get_user(db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
