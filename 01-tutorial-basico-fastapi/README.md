# Repaso Tutorial Básico de FastAPI (User Guide Core)

## Visión general

Estas lecciones cubren el núcleo de cómo se modelan entradas y salidas en FastAPI usando tipos de Python y modelos Pydantic: rutas básicas, path y query params, cuerpos de petición (simples, múltiples y anidados), validaciones y tipos de datos extra como `UUID` o `datetime`.

En esencia: defines funciones de Python con type hints, y FastAPI se encarga de parsear, validar y documentar automáticamente la API.

---

## Primeros pasos y rutas básicas

- Creas una app con:

  ```python
  from fastapi import FastAPI

  app = FastAPI()
  ```

- Defines un endpoint con un decorador y una función:

  ```python
  @app.get("/")
  async def root():
      return {"message": "Hello World"}
  ```

- La función bajo el decorador es la "path operation function"; FastAPI la ejecuta cuando recibe una petición para esa ruta y método HTTP.
- Puedes ejecutar el servidor en local con:

  ```bash
  uvicorn main:app --reload
  ```

  o con la CLI de FastAPI:

  ```bash
  fastapi dev
  ```

- Visita `http://127.0.0.1:8000` y verás el JSON `{"message": "Hello World"}`.
- La documentación interactiva se muestra automáticamente en `/docs` (Swagger UI) y `/redoc`.
- El esquema OpenAPI generado está disponible en `/openapi.json`.
- Puedes configurar el entrypoint en `pyproject.toml` con:

  ```toml
  [tool.fastapi]
  entrypoint = "main:app"
  ```

  para que `fastapi dev` y otras herramientas (VS Code, FastAPI Cloud) encuentren tu aplicación sin tener que pasar la ruta manualmente.

- `fastapi deploy` es una opción adicional si quieres desplegar la app rápidamente a FastAPI Cloud.

- Los parámetros de la función se convierten en partes de la API:
  - Si están en la ruta, son **path params**.
  - Si no están en la ruta ni son modelos, por defecto son **query params**.
  - Si son modelos Pydantic, se interpretan como **cuerpo (body)** de la petición.

La documentación automática se genera en `/docs` (Swagger UI) y `/redoc` usando OpenAPI.

---

## Path parameters y validaciones numéricas

- Los path params se definen incluyendo `{nombre}` en la ruta, por ejemplo `"/items/{item_id}"`, y tipándolos en la función: `item_id: int`.  
- Para validaciones numéricas sobre path params se usa `Path(...)`, por ejemplo:
  - `ge`, `gt`, `le`, `lt` para límites.
  - Metadatos como `title`, `description` y `example`.

FastAPI convierte tipos automáticamente y devuelve errores 422 si el dato no cumple el tipo o las restricciones.

---

## Query parameters y validaciones de string / modelos

- Cualquier parámetro que:
  - no va en la ruta,
  - no es modelo Pydantic,
  - y no se marca explícitamente como body,

  se trata como **query parameter**.

- Con `Query(...)` puedes:
  - Definir valores por defecto.
  - Hacerlos opcionales (`Optional[str]`).
  - Añadir restricciones: longitud mínima/máxima, regex, etc.
  - Añadir metadatos: alias, título, descripción, ejemplo.

- Para agrupar varios query params, puedes definir un modelo Pydantic (por ejemplo `SearchFilters`) y recibirlo como un solo objeto, manteniendo validación y documentación.

---

## Request body: modelos, múltiples parámetros y campos

- Un modelo Pydantic (`class Item(BaseModel): ...`) se usa como tipo para representar el JSON del cuerpo de la petición.  
- Puedes mezclar:
  - Path params.
  - Query params.
  - Uno o varios cuerpos (varios modelos de body en la misma operación).

Cuando hay varios modelos en el body, FastAPI los agrupa en un JSON con claves por modelo o por el nombre del parámetro, según cómo lo declares.

- `Body(...)` permite:
  - Forzar que un valor simple se trate como body.
  - Configurar metadata similar a `Query`/`Path` (descripción, ejemplo, etc.).

### Fields en modelos (Body - Fields)

Dentro de los modelos Pydantic, `Field(...)` se usa para:

- Establecer valores por defecto.
- Añadir restricciones (longitud, límites, regex).
- Definir alias (nombre diferente en JSON).
- Añadir metadatos: título, descripción, ejemplo, `deprecated`, etc.

---

## Modelos anidados y datos de ejemplo

### Modelos anidados

- Los cuerpos pueden ser modelos anidados:
  - Un modelo puede contener otros modelos.
  - Listas de modelos (`list[SubModel]`).
  - Diccionarios tipados (`dict[str, SubModel]`).

FastAPI valida de forma recursiva toda la estructura anidada y genera el esquema completo en la documentación.

### Declarar datos de ejemplo

Puedes declarar ejemplos de varias formas:

- En el modelo (a través de la configuración o `Field`).
- En el endpoint, usando `example` o `examples` en `Body` y otros helpers.

En la lección se destaca un detalle técnico importante: FastAPI 0.99+ usa OpenAPI 3.1.0 y JSON Schema 2020-12, lo que permite que los ejemplos declarados en Pydantic y en los parámetros de request se integren de forma más consistente. También existe el parámetro `openapi_examples` para declarar múltiples ejemplos con metadatos adicionales en la documentación.

Estos ejemplos se muestran en Swagger UI como payload de muestra, lo que ayuda a otros (frontend, QA, etc.) a entender cómo consumir la API.

---

## Tipos de datos extra

Además de `int`, `float`, `str` y `bool`, FastAPI soporta tipos más ricos con conversión, validación y documentación automáticas:

- `uuid.UUID`  
- `datetime.datetime`, `datetime.date`, `datetime.time` (formato ISO 8601 en JSON).  
- `datetime.timedelta` para duraciones, normalmente representadas como segundos.  
- `Decimal` para valores numéricos con precisión fija.  
- `bytes` (JSON los representa como cadenas base64).  
- `set` y `frozenset` (se serializan como listas pero se validan como conjuntos).

Todo esto queda reflejado en el esquema OpenAPI y en la documentación interactiva.

---

## Regla mental clave

Una forma rápida de recordar cómo trata FastAPI los parámetros:

- Lo que aparece en la ruta (`/items/{item_id}`) → **path param**.  
- Lo que está en la firma y no está en la ruta ni es modelo → **query param**.  
- Lo que es modelo Pydantic (o se marca explícitamente como `Body`) → **request body**.
