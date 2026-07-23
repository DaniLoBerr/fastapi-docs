# Resumen Parte 3 - Special params

---

## Parámetros de Cookie

### Idea general

La lección muestra cómo leer cookies de las peticiones HTTP en FastAPI usando el tipo especial `Cookie`, siguiendo el mismo patrón que `Query` y `Path` para parámetros de consulta y de ruta.

### Importar `Cookie`

Para empezar, se importa `Cookie` y se define la aplicación:

```python
from typing import Annotated
from fastapi import Cookie, FastAPI

app = FastAPI()
```

También se muestra la forma alternativa sin `Annotated`:

```python
from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
```

En ambos casos, `ads_id` se lee desde una cookie llamada `ads_id` enviada por el cliente.

### Declarar parámetros de cookie

Los parámetros de cookie se declaran igual que los de `Path` y `Query`, y admiten valores por defecto, tipos y validación extra.

Ejemplo con `Annotated`:

```python
@app.get("/items/")
async def read_items(
    ads_id: Annotated[str | None, Cookie()] = None
):
    return {"ads_id": ads_id}
```

`Cookie` es un “pariente” de `Query` y `Path`, heredando del mismo tipo base `Param`, así que comparte su comportamiento de anotación y validación.

### Nota importante

Para que FastAPI trate un parámetro como cookie, es obligatorio usar `Cookie`; si no, el parámetro se interpretará como parámetro de query de forma automática.

### Resumen

- Se usan cookies como otra fuente de parámetros de entrada del cliente.
- Se declaran con `Cookie`, con el mismo patrón que `Query` y `Path`.
- Se pueden usar tanto con `Annotated[...]` como con la forma clásica `param = Cookie(default=...)`.

---

## Parámetros de Header en FastAPI

La lección trata sobre cómo leer parámetros de cabecera HTTP en FastAPI usando el tipo especial `Header`, de forma muy similar a `Query`, `Path` y `Cookie`.

### Declarar parámetros de header

- Importa `Header` y úsalo junto con `Annotated` para el parámetro de la función de ruta.  
- Al usar `Header(...)` en el valor por defecto, FastAPI entiende que ese parámetro se obtiene de los headers de la petición.  
- Puedes usar valores por defecto, validaciones, etc., igual que con `Query`, `Path` y `Cookie`, porque `Header` se basa en la misma clase `Param`.

### Conversión de nombres: underscores → hyphens

- Los headers HTTP usan guiones (`user-agent`), mientras que en Python se usan variables con guiones bajos (`user_agent`).  
- FastAPI convierte automáticamente los guiones bajos del nombre del parámetro en guiones al buscar el header real.  
- Esta conversión se puede desactivar pasando `convert_underscores=False` a `Header` si necesitas el nombre exacto tal cual.

### Headers con múltiples valores

- Algunos headers pueden aparecer varias veces o contener varios valores.  
- Para estos casos, puedes declarar el parámetro como `List[str]` (u otra lista) y FastAPI devolverá todos los valores en esa lista en lugar de uno solo.

### Ideas clave

- Usa `Header` para leer valores de encabezados HTTP de forma declarativa, igual que `Query` o `Path`.  
- Aprovecha la conversión automática de `snake_case` a nombres de header con guiones, salvo que necesites desactivarla con `convert_underscores=False`.

---

## Modelos de Cookies en FastAPI

### Idea principal

La lección de **Cookie Parameter Models** explica que, si tu aplicación usa varias cookies relacionadas entre sí, puedes agruparlas en un **modelo de Pydantic** en lugar de declararlas una por una como parámetros sueltos.

### Cómo se hace

- Defines un **modelo Pydantic** con los campos que representan cada cookie (por ejemplo `session_id`, `theme`, etc.).
- En la función de ruta, anotas un parámetro con ese modelo y lo marcas como `Cookie(...)` (normalmente usando `typing.Annotated`).
- FastAPI:
  - Lee las cookies del `Request`
  - Extrae los valores para cada campo
  - Construye automáticamente una instancia del modelo que recibes **ya validada**.

### Ventajas y validación extra

- Puedes **reutilizar** el mismo modelo en varias rutas que compartan las mismas cookies.
- Puedes añadir **validaciones** y metadatos a nivel de modelo, igual que con otros modelos de Pydantic.
- Si quieres rechazar cookies inesperadas, puedes usar la configuración del modelo (`extra = "forbid"`) para **prohibir campos extra**.

### Resumen en una frase

Puedes usar **modelos de Pydantic** para declarar grupos de cookies en FastAPI, reutilizar esa definición en varias rutas y centralizar la validación y las reglas sobre esas cookies.