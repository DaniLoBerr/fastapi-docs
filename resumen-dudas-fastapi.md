# Resumen de dudas sobre FastAPI y backend web

Documento vivo para ir acumulando respuestas cortas y claras sobre el tutorial de FastAPI y conceptos generales de desarrollo web. Está escrito para alguien que empieza desde cero, con lenguaje simple, ejemplos cotidianos y alguna metáfora para hacerlo más fácil de entender.

Nota: este resumen está alineado con la documentación oficial consultada el 2 de agosto de 2026.

## 1. Tipos genéricos vs modelos Pydantic

- Usa un `BaseModel` cuando el dato es como una ficha con varias casillas: nombre, precio, estado, fecha, etc.
- Usa un tipo simple o genérico (`list[...]`, `dict[...]`, `int`, `str`, `UUID`, `datetime`, `Enum`, etc.) cuando el dato es una lista, un mapa o un valor suelto.
- FastAPI puede trabajar con ambos en entrada y salida. Lo importante es la forma real del dato.
- Si por dentro manejas una cosa de una manera, pero hacia fuera quieres mostrar otra más limpia, usa `response_model`.
- Regla fácil: si parece una ficha de varios campos, piensa en modelo; si parece una lista o una sola pieza, piensa en tipo simple.

Piensa en un `BaseModel` como una caja con compartimentos. Un tipo simple es como una caja donde solo guardas una cosa.

Ejemplo útil:

```python
@app.get("/items/", response_model=list[Item])
async def read_items() -> list[Item]:
    ...
```

## 2. Cuándo usar asincronía

- Usa `async def` cuando tu código vaya a esperar algo que está fuera de Python, como una API, una base de datos asíncrona o una cola de mensajes.
- Usa `def` normal cuando el código o la librería son bloqueantes.
- FastAPI manda las funciones `def` a un grupo de trabajo aparte para no frenar el resto.
- No uses `async def` solo porque suena moderno. Si dentro haces llamadas bloqueantes, sigues frenando el programa.
- Para tareas muy pesadas de cálculo, ni `async` ni `def` bastan por sí solos; suele hacer falta usar procesos, workers o colas.

Idea corta: `async` no sirve para correr más rápido, sirve para no quedarse parado mientras espera.

## 3. Qué es el event loop

- El event loop es el que reparte turnos entre tareas asíncronas.
- Su trabajo es dejar que una tarea se pause cuando hace `await` y seguir con otra mientras espera.
- Si una tarea está esperando, el loop aprovecha para atender otras.
- Si metes una operación bloqueante dentro de una corrutina, es como poner un coche en mitad de una calle de un solo carril.

Piensa en él como un camarero muy rápido que va pasando por las mesas y atendiendo a quien ya está listo.

## 4. Cuándo usar variables de entorno

- Úsalas para cosas que cambian según el sitio donde corre la app: claves API, URLs, credenciales, puertos, nombre del entorno, flags de despliegue, etc.
- No las uses para datos de negocio que forman parte de la lógica de la aplicación.
- Son la forma habitual de separar código y configuración.
- Ayudan a no dejar secretos escritos dentro del repo y a reutilizar la misma app en desarrollo, pruebas y producción.
- En FastAPI, lo normal es leerlas con settings o con `os.getenv(...)`.

Ejemplos típicos: `DATABASE_URL`, `SECRET_KEY`, `OPENAI_API_KEY`, `ENVIRONMENT`, `OPENAPI_URL`.

## 5. Cómo crear un entorno con `uv`

- Si empiezas desde cero, `uv init` crea el proyecto.
- Si el proyecto ya existe, `uv venv` crea el entorno virtual `.venv`.
- `uv add "fastapi[standard]"` añade FastAPI y sus extras habituales.
- `uv sync` crea o actualiza `.venv` según `pyproject.toml` y `uv.lock`.
- `uv run ...` ejecuta comandos dentro del entorno sin activarlo a mano.

Flujo típico:

```bash
uv init
uv add "fastapi[standard]"
uv sync
uv run fastapi dev
```

Ventajas principales:

- Es muy rápido instalando y resolviendo dependencias.
- Deja un `uv.lock` para repetir el mismo entorno después.
- Maneja `.venv` de forma integrada.
- Hace más simple trabajar con scripts y comandos.
- Reduce bastante la gestión manual de `pip` y `venv`.

Piensa en `uv` como una caja de herramientas que monta y mantiene tu espacio de trabajo sin que tengas que hacerlo todo a mano.

## 6. Cómo funciona una app web moderna

- El cliente suele ser el navegador, una app móvil o un frontend.
- La petición viaja por HTTP hacia un proxy o balanceador, si existe.
- Detrás hay un servidor ASGI, como Uvicorn, que ejecuta tu aplicación FastAPI.
- FastAPI recibe la petición, resuelve dependencias, ejecuta middleware y llama a la función de la ruta.
- La respuesta se convierte al formato correcto, pasa otra vez por el middleware y vuelve al cliente.

Esquema mental:

```text
cliente -> proxy/load balancer -> servidor ASGI -> FastAPI
        -> middleware -> ruta/dependencias -> respuesta JSON
        -> middleware -> servidor ASGI -> cliente
```

Es como un restaurante: el cliente pide, el camarero lleva el pedido a cocina, cocina prepara la comida, el camarero la trae de vuelta.

## 7. `fastapi dev` vs `fastapi run`

- `fastapi dev` es para trabajar en desarrollo.
- Tiene recarga automática y suele escuchar en `127.0.0.1`.
- `fastapi run` es para producción.
- No activa recarga automática y suele escuchar en `0.0.0.0`.
- En producción normalmente va detrás de un proxy que se encarga de HTTPS y, muchas veces, de repartir tráfico entre varios procesos.

Regla rápida: `dev` es modo práctica; `run` es modo abierto al público.

## 8. Cuándo usar path parameters y cuándo query parameters

- Usa path parameters cuando el valor identifica al recurso: `/users/{user_id}`.
- Usa query parameters cuando el valor filtra, ordena, pagina o cambia cómo miras el recurso: `?skip=10&limit=20`.
- Los path params son obligatorios porque forman parte de la ruta.
- Los query params suelen ser opcionales y pueden tener valores por defecto.
- Si algo cambia qué recurso es, va en la ruta; si solo cambia cómo lo consultas, va en la query.

Piensa en la ruta como la dirección de una casa y en la query como los filtros de una búsqueda de catálogo.

## 9. Cuándo utilizar enums

- Usa `Enum` cuando el valor posible sale de una lista cerrada y conocida.
- Sirve mucho para estados, roles, categorías, ordenaciones y flags.
- Si quieres que el valor se vea como texto en la API y en la documentación, suele ir bien heredar de `str` y `Enum`.
- No lo uses para datos que cambian mucho o que vienen de una tabla viva en base de datos.

Ejemplo típico:

```python
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
```

Piensa en un `Enum` como el menú de un restaurante: puedes elegir entre unas pocas opciones, no inventarte una nueva en cada pedido.

## 10. Cuándo enviar datos en body y cuándo en form

- Usa body JSON cuando el cliente envía datos estructurados a una API.
- En FastAPI, lo normal es usar body en `POST`, `PUT`, `PATCH` y `DELETE`.
- Usa `Form` cuando el cliente manda datos como formulario HTML o cuando el flujo lo pide, por ejemplo en OAuth2 password flow.
- Si hay archivos, normalmente el envío es `multipart/form-data`, así que también entra en la familia de formularios.
- Un body en `GET` existe en teoría, pero está desaconsejado y suele dar problemas.

Piensa en JSON como una caja bien ordenada con etiquetas. Un formulario es más como rellenar campos en un mostrador.

## 11. Cuándo utilizar body fields

- Usa `Field(...)` dentro de un modelo Pydantic para poner reglas y descripción sobre una propiedad concreta.
- Es la opción natural cuando el dato forma parte del esquema del modelo.
- Úsalo para valores por defecto, `gt`, `ge`, `min_length`, `max_length`, `alias`, `description`, `examples`, `deprecated`, etc.
- Usa `Body(...)` en la firma de la función cuando el parámetro está en el body, pero no quieres o no puedes meterlo en un `BaseModel`.
- `Body` también sirve para cambiar la forma del payload o añadir metadatos al body completo.
- `Field` viene de `pydantic`, no de `fastapi`.

Ejemplo mental:

```python
class Item(BaseModel):
    name: str = Field(..., max_length=100)
    price: float = Field(gt=0)
```

Piensa en `Field` como las reglas de una casilla concreta y en `Body` como las reglas del paquete entero.

## 12. Cuándo usar `embed` en `Body`

- Usa `embed=True` cuando quieres que un único body venga envuelto en una clave.
- Te sirve si quieres un JSON con forma `{"item": {...}}` en lugar de `{"name": "...", ...}`.
- También ayuda si quieres mantener una forma parecida entre un endpoint con un solo body y otro con varios.
- Suele usarse por compatibilidad con contratos ya existentes o por claridad.

Ejemplo:

```python
item: Annotated[Item, Body(embed=True)]
```

Piensa en `embed=True` como meter la cosa dentro de una caja con etiqueta, en vez de enviarla suelta.

## 13. Cuándo recomendar `examples`

- Usa ejemplos cuando el payload es complejo, cuando hay varios equipos consumiendo la API o cuando quieres quitar dudas en Swagger UI.
- Son muy útiles en modelos anidados, arrays de objetos, enums y payloads con muchas reglas.
- Si el ejemplo pertenece al esquema del dato, usa `examples` en `Field(...)` o en `model_config = {"json_schema_extra": {"examples": [...]}}`.
- Si quieres varios ejemplos con nombre y metadatos para la operación, usa `openapi_examples` en `Body`, `Query`, `Path`, `Form`, `File`, etc.
- Si solo necesitas un ejemplo simple por compatibilidad, existe `example`, pero en FastAPI moderno suele ser mejor pensar primero en `examples` u `openapi_examples`.

Un ejemplo claro funciona como una foto del plato terminado: ayuda a entender el resultado sin tener que imaginarlo.

## 14. Cuándo usar `include_in_schema`

- Úsalo para ocultar una ruta o un parámetro de la documentación OpenAPI generada.
- Sirve para rutas internas, experimentales, de transición o para parámetros de depuración que no quieres enseñar.
- No lo uses como seguridad. Ocultar algo en la documentación no lo protege.
- Si quieres ocultar toda la documentación en un entorno, normalmente es mejor desactivar OpenAPI o las URLs de docs con configuración de la app.

Piensa en ello como quitar una puerta del mapa, no como poner un candado.

## 15. Cuándo usar `before` y `after` validators

- Usa `before` cuando necesites limpiar o adaptar la entrada antes de que Pydantic la entienda.
- Sirve para aceptar formatos flexibles, datos viejos o valores sucios que quieras convertir.
- En validadores de modelo, `mode="before"` sirve para revisar el diccionario crudo antes de construir el modelo.
- Usa `after` cuando el valor ya está validado y solo quieres comprobar reglas, coherencia o relaciones entre campos.
- En validadores de modelo, `mode="after"` es útil para revisar el objeto una vez creado.
- `after` suele ser más simple y seguro porque ya trabajas con tipos correctos.
- Evita `before` en campos discriminadores de un `Union` discriminado, porque puede romper la elección del tipo correcto.

Regla rápida:

- `before` = limpiar la entrada.
- `after` = revisar el resultado ya limpio.

Piensa en ello como lavar ingredientes antes de cocinar y probar la comida al final.

## 16. Orden de parámetros y uso de `*`

- Python exige que los parámetros sin valor por defecto vayan antes que los que sí tienen.
- FastAPI identifica los parámetros por nombre, tipo y marcador (`Query`, `Path`, `Body`, etc.), no solo por el orden.
- Si necesitas ordenar la firma de forma más flexible sin perder claridad, puedes usar `*` para obligar a pasar parámetros por nombre.
- En FastAPI moderno, `Annotated` reduce bastante la necesidad de trucos con el orden.

Ejemplo:

```python
async def read_items(*, item_id: int = Path(...), q: str):
    ...
```

Piensa en `*` como una señal que dice: "a partir de aquí, di claramente el nombre de cada cosa".

## 17. Cuándo usar un modelo Pydantic y cuándo un tipo "arbitrario"

- Usa un modelo Pydantic cuando el dato tiene estructura clara, varios campos, validaciones propias y quieres reutilizarlo.
- Usa un tipo concreto o genérico cuando el payload es naturalmente una lista, un diccionario o un valor simple.
- Usa `UUID`, `datetime`, `Decimal`, `Enum`, `HttpUrl`, `EmailStr` y tipos parecidos cuando describen mejor el dato que un `str` genérico.
- Si el objeto no es fácil de convertir a JSON o no tiene una forma clara de esquema, normalmente conviene transformarlo antes de exponerlo por la API.
- En FastAPI, muchas veces la mejor respuesta es: modelo para la forma pública del recurso; tipos genéricos para colecciones y valores puntuales.

## 18. Framework, ORM y herramientas de migración

- Un framework web se encarga de la ruta completa de la petición: rutas, dependencias, middleware y respuesta.
- Un ORM se encarga de traducir objetos de Python a tablas y filas de base de datos, y al revés.
- Una herramienta de migraciones guarda el historial de cambios de la base de datos y permite aplicarlos o deshacerlos de forma controlada.
- FastAPI no sustituye al ORM ni a las migraciones.
- Lo normal es usar las tres piezas juntas: FastAPI + ORM + migraciones.

Ejemplos mentales:

- Framework: FastAPI.
- ORM: SQLAlchemy o SQLModel.
- Migraciones: Alembic.

Piensa en el framework como la estructura de la casa, el ORM como el traductor entre tu código y la base de datos, y las migraciones como el historial de reformas.

## 19. Qué es una importación circular

- Ocurre cuando dos módulos se importan entre sí, de forma directa o indirecta.
- Python empieza a cargar un módulo y, antes de terminar, intenta cargar el otro, que vuelve a pedir algo del primero.
- El error típico habla de un `partially initialized module` o muestra un `ImportError` parecido.
- En FastAPI pasa mucho cuando `main.py` importa `routers.py` y `routers.py` vuelve a importar `main.py`.
- La solución suele ser mover el código compartido a otro módulo, retrasar imports hasta dentro de funciones o cambiar la dirección de las dependencias.

Regla práctica: evita que routers, modelos y dependencias dependan del archivo principal de la app.

## 20. Reglas rápidas para recordar

- Si el dato identifica el recurso, va en la ruta.
- Si el dato filtra o cambia la consulta, va en query.
- Si el dato es JSON estructurado, piensa en body y Pydantic.
- Si el dato viene de un formulario HTML, piensa en `Form`.
- Si el código espera I/O, piensa en `async`.
- Si la configuración cambia según el entorno, piensa en variable de entorno.
- Si el valor pertenece a un conjunto cerrado, piensa en `Enum`.
- Si quieres ocultarlo de OpenAPI, piensa en `include_in_schema=False`.

## 21. Fuentes oficiales consultadas

- FastAPI CLI: https://fastapi.tiangolo.com/fastapi-cli/
- Response Model - Return Type: https://fastapi.tiangolo.com/tutorial/response-model/
- Request Body: https://fastapi.tiangolo.com/tutorial/body/
- Body - Multiple Parameters: https://fastapi.tiangolo.com/tutorial/body-multiple-params/
- Path Parameters and Numeric Validations: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
- Query Parameters and String Validations: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
- Form Data: https://fastapi.tiangolo.com/tutorial/request-forms/
- Declare Request Example Data: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
- Path Operation Configuration: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
- Path Operation Advanced Configuration: https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/
- Pydantic Validators: https://docs.pydantic.dev/latest/concepts/validators/
- asyncio: https://docs.python.org/3/library/asyncio.html
- Event loop: https://docs.python.org/3/library/asyncio-eventloop.html
- uv project layout: https://docs.astral.sh/uv/concepts/projects/layout/
