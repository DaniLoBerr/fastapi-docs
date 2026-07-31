# Resumen de Parámetros Especiales, Modelos en Capas y Respuestas

Este README resume las lecciones de esta carpeta sobre `Cookie`, `Header`, modelos de cookies y cabeceras, modelos de respuesta, uso de `response_model` y configuración de `status_code`.

---

## 1. Cookie Parameters

- `Cookie` permite leer cookies de la petición HTTP igual que `Query` y `Path` permiten leer otros parámetros.
- Si no usas `Cookie`, FastAPI interpreta el parámetro como query param.
- Se puede usar con `Annotated[...]` o con la forma clásica `param = Cookie(default=...)`.
- El navegador y la UI de `/docs` no hacen fácil enviar cookies arbitrarias desde la documentación interactiva, así que aunque rellenes el formulario, la cookie puede no llegar como esperas.

### Idea rápida

Usa `Cookie()` cuando el dato venga almacenado en una cookie del cliente.

---

## 2. Header Parameters

- `Header` sirve para leer cabeceras HTTP de forma declarativa.
- Funciona con el mismo patrón que `Query`, `Path` y `Cookie`.
- FastAPI convierte automáticamente los nombres de parámetros con guiones bajos a nombres de header con guiones.
  - `user_agent` se busca como `User-Agent`
- Si necesitas desactivar esa conversión, puedes usar `convert_underscores=False`.
- Si una cabecera puede repetirse varias veces, puedes declararla como `list[str]` para recibir todos sus valores.

### Idea rápida

Usa `Header()` para metadatos de la request como `User-Agent`, tokens o cabeceras personalizadas.

---

## 3. Cookie Parameter Models

- Si varias cookies están relacionadas, puedes agruparlas en un modelo Pydantic.
- Esto permite reutilizar el mismo modelo en varias rutas.
- También centraliza validaciones y metadatos.
- Puedes prohibir cookies extra con `model_config = {"extra": "forbid"}`.

### Ventaja principal

En vez de declarar cookies una a una, defines un modelo y FastAPI construye la instancia validada automáticamente.

---

## 4. Header Parameter Models

- Igual que con cookies, puedes agrupar cabeceras relacionadas en un modelo Pydantic.
- FastAPI rellena el modelo a partir de los headers de la petición.
- Puedes añadir validaciones y campos opcionales.
- También puedes prohibir cabeceras extra si lo necesitas.
- Si quieres mantener nombres exactos de cabecera, puedes desactivar la conversión de `snake_case` a `kebab-case`.

### Caso práctico

Útil cuando varias rutas comparten un conjunto fijo de cabeceras como `host`, `save-data`, `if-modified-since`, `traceparent` o listas tipo `X-Tag`.

---

## 5. Response Model y Return Type

FastAPI usa el tipo de retorno y/o `response_model` para varias cosas:

- validar el dato devuelto
- generar JSON Schema
- serializar la respuesta
- filtrar campos de salida

### `response_model`

- Se usa cuando quieres devolver algo que no coincide exactamente con la anotación de retorno.
- Es muy útil si devuelves un `dict` pero quieres documentarlo como un modelo Pydantic.
- `response_model` tiene prioridad sobre la anotación del tipo de retorno.
- Si tu editor se queja, puedes anotar el retorno como `Any` y dejar que FastAPI use `response_model`.
- También puedes desactivar el modelo con `response_model=None`.

### Modelos de entrada y salida diferentes

- Es una buena práctica separar modelos según su uso:
  - uno para entrada
  - otro para salida
  - otro para datos persistidos en BD
- Esto evita devolver campos sensibles como contraseñas.

### Filtrado de salida

FastAPI permite filtrar la respuesta con:

- `response_model_exclude_unset=True`
- `response_model_exclude_defaults=True`
- `response_model_exclude_none=True`
- `response_model_include={...}`
- `response_model_exclude={...}`

### Resumen mental

Si lo que devuelves no encaja exactamente con el tipo anotado, usa `response_model` para que la documentación y la validación sigan siendo correctas.

---

## 6. Extra Models

- FastAPI anima a evitar duplicación de modelos.
- Si una entidad tiene “estados” distintos, es mejor crear varios modelos relacionados por herencia.

### Patrón típico con usuarios

- `UserBase`: campos comunes
- `UserIn`: campos de entrada, como `password`
- `UserOut`: campos de salida, sin contraseña
- `UserInDB`: representación en base de datos, con `hashed_password`

### Uniones de modelos

- Puedes usar `Model1 | Model2` o `Union[Model1, Model2]`.
- Cuando hay modelos parecidos, conviene poner primero el más específico.
- FastAPI genera el esquema como `anyOf` en OpenAPI.

### Diccionarios arbitrarios

- Si no conoces exactamente la estructura de la salida, puedes tiparla como `dict[str, str]` u otro diccionario genérico.
- También puedes devolver listas de modelos o combinaciones similares.

### Idea clave

No necesitas un único modelo por entidad. Puedes tener varios modelos para distintas fases del flujo: entrada, persistencia y salida.

---

## 7. Response Status Code

- `status_code` en el decorador de la ruta define el código HTTP de la respuesta.
- También queda documentado en OpenAPI.
- Puede ser:
  - un número, como `201`
  - un `IntEnum`, como `http.HTTPStatus`
  - una constante de `fastapi.status`

### Convención útil

- `200` para respuestas normales
- `201` para creación de recursos
- `404` para no encontrado
- `400` para errores del cliente
- `500` para errores del servidor

### Recomendación práctica

Usar `fastapi.status.HTTP_201_CREATED` mejora la legibilidad y el autocompletado.

---

## Resumen rápido

- `Cookie()` lee cookies.
- `Header()` lee cabeceras HTTP.
- Los modelos de cookies y cabeceras centralizan validación y reutilización.
- `response_model` controla documentación, validación y filtrado de salida.
- Separa modelos de entrada, salida y persistencia cuando tenga sentido.
- `status_code` documenta y fija el código HTTP de la respuesta.

