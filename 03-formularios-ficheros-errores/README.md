# Resumen de Formularios, Ficheros y Manejo de Errores en FastAPI

Este README recoge los apuntes de las lecciones de esta carpeta y resume las ideas clave sobre formularios, subida de ficheros, manejo de errores, configuración de rutas, codificación JSON y actualizaciones parciales del body.

---

## 1. Form Data

- Se usa cuando quieres recibir datos desde un formulario en lugar de JSON.
- `Form` funciona igual que `Body`, `Query`, `Path` o `Cookie` a nivel de configuración y validación.
- Si no marcas un parámetro como `Form`, FastAPI lo interpretará como `Query` por defecto.
- Los formularios HTML usan `application/x-www-form-urlencoded`.
- Los formularios con ficheros usan `multipart/form-data`.
- JSON usa `application/json`.
- No puedes mezclar parámetros `Body` y `Form` en la misma request.
- En OAuth2 password flow, el `username` y `password` deben llegar exactamente como campos de formulario con esos nombres.

### Idea mental

Si los datos vienen de un `<form>`, usa `Form()`.

---

## 2. Form Models

- Puedes agrupar los datos del formulario en un modelo Pydantic.
- Esto permite reutilizar validaciones y mantener el endpoint más limpio.
- También puedes prohibir campos extra con `model_config = {"extra": "forbid"}`.

### Ventaja principal

Un modelo Pydantic te da la misma validación de siempre, pero aplicada a datos de formulario.

---

## 3. Request Files

- Los ficheros también se envían como `form data`.
- `File` sirve para archivos pequeños que quieres leer como `bytes`.
- `UploadFile` es mejor para archivos grandes.

### `File`

- Carga el contenido en memoria RAM.
- Es útil cuando el archivo es pequeño.

### `UploadFile`

- Usa un archivo temporal tipo `SpooledTemporaryFile`.
- Se mantiene en memoria hasta cierto tamaño y luego pasa a disco.
- Permite acceder a metadatos como:
  - `filename`
  - `content-type`
  - `file`
- Tiene métodos asíncronos como `read()`, `write()`, `seek()` y `close()`.
- También puedes acceder de forma síncrona a través de `myfile.file.read()`.

### Otros apuntes

- Puedes recibir varios archivos en una lista.
- Tanto `File` como `UploadFile` pueden ser opcionales.
- Ambos admiten metadatos.

---

## 4. Requests with Forms and Files

- `Form` y `File` se pueden usar juntos en el mismo endpoint.
- Esto es útil para enviar un token o campos de texto junto con uno o varios archivos.

### Regla rápida

- Si es dato de formulario, usa `Form()`.
- Si es archivo, usa `File()` o `UploadFile()`.
- Si necesitas ambos, FastAPI los combina sin problema en la misma request.

---

## 5. Handling Errors

- La forma habitual de lanzar errores en FastAPI es con `HTTPException`.
- El campo `detail` puede ser cualquier dato serializable a JSON, no solo un string.
- También puedes añadir headers personalizados al error.

### Errores personalizados

- Puedes crear tus propias excepciones.
- Después puedes registrar un manejador global con `@app.exception_handler(...)`.
- Esto permite devolver una respuesta personalizada cuando se lance esa excepción.

### Sobrescribir handlers por defecto

- FastAPI maneja por defecto:
  - `HTTPException`
  - `RequestValidationError`
- Puedes cambiar su comportamiento si quieres devolver texto plano, mensajes de log u otro formato.
- Al sobrescribir `RequestValidationError`, el cambio afecta a toda la aplicación.
- Conviene no devolver información sensible en bruto al cliente.
- Si necesitas inspeccionar el cuerpo de una request inválida, `RequestValidationError` expone `body`.

### Reutilizar handlers

- Puedes capturar el comportamiento por defecto y reutilizarlo en tus propios handlers.
- Esto es útil si quieres añadir logging sin cambiar la respuesta final.

### Nota importante

- Para manejar `HTTPException`, la documentación recomienda usar la clase de Starlette, no la de FastAPI, para no perder excepciones lanzadas por Starlette.

---

## 6. Path Operation Configuration

FastAPI permite configurar bastante el decorador de cada ruta.

### 1. Status code

- Sirve para indicar el código HTTP de respuesta.
- También queda reflejado en OpenAPI.
- Ejemplo típico: `201 Created` en un `POST`.

### 2. Tags

- Sirven para agrupar y organizar endpoints en la documentación.
- Ayudan a que Swagger UI quede más legible.

### 3. Tags con enums

- Puedes usar `Enum` para evitar repetir cadenas y asegurar consistencia.

### 4. Summary y description

- `summary` da un título corto.
- `description` añade una explicación más larga.

### 5. Descripción en docstring

- También puedes escribir la descripción directamente en el docstring del endpoint.
- Se admite Markdown.

### 6. Response description

- Permite describir la respuesta en OpenAPI.
- Si no se especifica, FastAPI genera una descripción automática.

### 7. Deprecated

- Puedes marcar una ruta como obsoleta con `deprecated=True`.
- Así sigue visible en el esquema, pero indicando que no debería usarse.

---

## 7. JSON Compatible Encoder

- `jsonable_encoder` convierte objetos a un formato compatible con JSON.
- Es muy útil cuando quieres guardar datos en una base de datos o devolverlos en una respuesta JSON.
- Convierte tipos no serializables directamente, como `datetime` o `UUID`, a formatos compatibles.
- En modelos Pydantic, suele convertir el objeto a `dict`.

### Idea práctica

Si vas a persistir un modelo o devolverlo como JSON y contiene tipos especiales, pásalo por `jsonable_encoder`.

---

## 8. Body Updates

- `PUT` se usa para sustituir un recurso completo.
- `PATCH` se usa para actualizar solo algunos campos.

### Actualización parcial

- En Pydantic, `model_dump(exclude_unset=True)` permite obtener solo los campos que llegaron en la request.
- `model_copy(update=...)` permite crear una copia del modelo con cambios aplicados.

### Modelos separados

- Es recomendable tener:
  - un modelo para creación, con campos obligatorios
  - otro modelo para actualización, con campos opcionales

### Flujo típico

- Guardas el modelo usando `jsonable_encoder`.
- Para `PUT`, sustituyes el recurso completo.
- Para `PATCH`, recuperas el recurso actual, aplicas solo los cambios recibidos y vuelves a guardar.

---

## Resumen rápido

- `Form()` para formularios.
- `File()` y `UploadFile` para ficheros.
- `Form` y `File` pueden convivir en la misma request.
- `HTTPException` es la forma estándar de lanzar errores HTTP.
- Puedes crear y sobrescribir exception handlers.
- `status_code`, `tags`, `summary`, `description` y `deprecated` mejoran la documentación OpenAPI.
- `jsonable_encoder` convierte objetos a JSON compatible.
- `PUT` sustituye, `PATCH` actualiza parcialmente.
