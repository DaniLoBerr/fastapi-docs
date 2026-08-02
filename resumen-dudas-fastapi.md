# Resumen de dudas sobre FastAPI y backend web

Documento vivo para ir acumulando respuestas cortas y claras sobre el tutorial de FastAPI y conceptos generales de desarrollo web.

Nota: este resumen está alineado con la documentación oficial consultada el 2 de agosto de 2026.

## 1. Tipos genéricos vs modelos Pydantic

- Usa un `BaseModel` cuando el dato representa un objeto con identidad propia, varios campos, validación, anidación y documentación clara.
- Usa tipos genéricos o simples (`list[...]`, `dict[...]`, `int`, `str`, `UUID`, `datetime`, `Enum`, etc.) cuando la forma del dato es una colección, un mapa o un valor aislado.
- En entrada y salida, FastAPI puede trabajar con ambos. Lo importante es la forma real del dato y el contrato que quieres exponer.
- En respuestas, si lo que devuelves no coincide exactamente con el contrato público, usa `response_model` para separar la implementación interna de la API que ve el cliente.
- Regla mental: objeto de dominio -> modelo Pydantic; array, mapa o escalar -> tipo genérico o simple.

Ejemplo útil:

```python
@app.get("/items/", response_model=list[Item])
async def read_items() -> list[Item]:
    ...
```

## 2. Cuándo usar asincronía

- Usa `async def` cuando vayas a llamar a librerías realmente asíncronas y vayas a hacer `await` sobre I/O: HTTP, base de datos async, colas, etc.
- Usa `def` normal cuando tu código o la librería que usas es bloqueante.
- FastAPI ejecuta las funciones `def` en un threadpool para no bloquear el event loop.
- No uses `async def` solo "porque sí": si dentro haces llamadas bloqueantes, el event loop se queda bloqueado igual.
- Para trabajo CPU-bound pesado, ni `async` ni `def` son la solución por sí solos; suele hacer falta mover trabajo a procesos, workers o colas.

Idea corta: `async` sirve para esperar sin bloquear; no sirve para acelerar cómputo puro.

## 3. Qué es el event loop

- El event loop es el núcleo de `asyncio`.
- Su trabajo es coordinar tareas, suspender corrutinas cuando hacen `await` y reanudarlas cuando el resultado está listo.
- Mientras una tarea espera I/O, el loop puede atender otras.
- Si metes una operación bloqueante dentro de una corrutina, paras esa ventaja.

Piensa en él como el "planificador" que decide qué tarea corre en cada momento.

## 4. Cuándo usar variables de entorno

- Úsalas para configuración que cambia según el entorno: claves API, URLs, credenciales, puertos, flags de despliegue, nombre del entorno, etc.
- No las uses para datos de negocio que pertenecen a la lógica de la aplicación.
- Son la forma habitual de separar código y configuración.
- Ayudan a no hardcodear secretos en el repo y a reutilizar la misma app en desarrollo, staging y producción.
- En FastAPI, lo normal es leerlas a través de settings o `os.getenv(...)`.

Ejemplos típicos: `DATABASE_URL`, `SECRET_KEY`, `OPENAI_API_KEY`, `ENVIRONMENT`, `OPENAPI_URL`.

## 5. Cómo crear un entorno con `uv`

- Si partes de cero, `uv init` crea el proyecto.
- Si el proyecto ya existe, `uv venv` crea el entorno virtual `.venv`.
- `uv add "fastapi[standard]"` añade FastAPI y sus extras habituales al proyecto.
- `uv sync` crea o actualiza `.venv` según `pyproject.toml` y `uv.lock`.
- `uv run ...` ejecuta comandos dentro del entorno del proyecto sin activarlo manualmente.

Flujo típico:

```bash
uv init
uv add "fastapi[standard]"
uv sync
uv run fastapi dev
```

Ventajas principales:

- Muy rápido instalando y resolviendo dependencias.
- Genera un `uv.lock` reproducible.
- Maneja `.venv` de forma integrada.
- Hace más simple trabajar con scripts, proyectos y comandos.
- Reduce bastante la gestión manual de `pip` y `venv`.

## 6. Cómo funciona una app web moderna

- El cliente suele ser el navegador, una app móvil o un frontend SPA.
- La petición viaja por HTTP hacia un proxy o balanceador, si existe.
- Detrás hay un servidor ASGI, como Uvicorn, que ejecuta tu aplicación FastAPI.
- FastAPI recibe la petición, resuelve dependencias, ejecuta middleware y llama a la función de ruta.
- La respuesta se serializa, se pasa otra vez por la cadena de middleware y vuelve al cliente.

Esquema mental:

```text
cliente -> proxy/load balancer -> servidor ASGI -> FastAPI
        -> middleware -> ruta/dependencias -> respuesta JSON
        -> middleware -> servidor ASGI -> cliente
```

## 7. `fastapi dev` vs `fastapi run`

- `fastapi dev` es para desarrollo.
- Tiene auto-reload por defecto y escucha en `127.0.0.1`.
- `fastapi run` es para producción.
- No activa auto-reload por defecto y escucha en `0.0.0.0`.
- En producción normalmente se usa detrás de un proxy/reverse proxy que gestione HTTPS y, muchas veces, varios workers.

Regla rápida: `dev` para iterar localmente; `run` para exponer la app de forma real.

## 8. Cuándo usar path parameters y cuándo query parameters

- Usa path parameters cuando el valor identifica el recurso: `/users/{user_id}`.
- Usa query parameters cuando el valor filtra, ordena, pagina o modifica la vista del recurso: `?skip=10&limit=20`.
- Los path params son obligatorios porque forman parte de la ruta.
- Los query params son opcionales por naturaleza y pueden tener valores por defecto.
- Si algo cambia la identidad del recurso, va en la ruta; si solo cambia cómo lo consultas, va en la query.

## 9. Cuándo utilizar enums

- Usa `Enum` cuando el valor posible pertenece a un conjunto cerrado y conocido.
- Son muy útiles para estados, roles, categorías, ordenaciones, flags y valores de ruta fijos.
- Si quieres que el valor se vea como texto en API y documentación, suele ser buena idea heredar de `str` y `Enum`.
- No los uses para datos que cambian con frecuencia o que vienen de una tabla viva en base de datos.

Ejemplo típico:

```python
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
```

## 10. Cuándo enviar datos en body y cuándo en form

- Usa body JSON cuando el cliente envía datos estructurados a una API: es el caso más habitual.
- En FastAPI, lo normal es usar body en `POST`, `PUT`, `PATCH` y `DELETE`.
- Usa `Form` cuando el cliente manda datos como formulario HTML o cuando el protocolo lo exige, por ejemplo OAuth2 password flow.
- Si hay archivos, el envío suele ser `multipart/form-data`, así que también entras en la familia de formularios.
- Un body en `GET` existe en la práctica, pero está desaconsejado y da problemas de interoperabilidad.

## 11. Cuándo utilizar body fields

- Usa `Field(...)` dentro de un modelo Pydantic para poner validación y metadata sobre un atributo concreto.
- Es la opción natural cuando el dato forma parte del esquema del modelo.
- Úsalo para defaults, `gt`, `ge`, `min_length`, `max_length`, `alias`, `description`, `examples`, `deprecated`, etc.
- Usa `Body(...)` en la firma de la función cuando el parámetro está en el body pero no quieres o no puedes modelarlo como un `BaseModel`.
- `Body` también sirve para cambiar la forma del payload o añadir metadata al body completo.
- `Field` viene de `pydantic`, no de `fastapi`.

Ejemplo mental:

```python
class Item(BaseModel):
    name: str = Field(..., max_length=100)
    price: float = Field(gt=0)
```

## 12. Cuándo usar `embed` en `Body`

- Usa `embed=True` cuando quieres que un único body vaya envuelto en una clave.
- Es útil si quieres que el JSON tenga forma `{"item": {...}}` en vez de `{"name": "...", ...}`.
- También ayuda si quieres mantener una forma consistente entre un endpoint con un solo body y otro con varios cuerpos.
- Suele usarse por compatibilidad con contratos existentes o por claridad semántica.

Ejemplo:

```python
item: Annotated[Item, Body(embed=True)]
```

## 13. Cuándo recomendar `examples`

- Usa ejemplos cuando el payload es complejo, cuando hay varios equipos consumiendo la API o cuando quieres reducir dudas en Swagger UI.
- Son muy útiles en modelos anidados, arrays de objetos, enums y payloads con muchas restricciones.
- Si el ejemplo pertenece al esquema del dato, usa `examples` en `Field(...)` o en `model_config = {"json_schema_extra": {"examples": [...]}}`.
- Si quieres varios ejemplos con nombre y metadatos para la operación, usa `openapi_examples` en `Body`, `Query`, `Path`, `Form`, `File`, etc.
- Si solo necesitas un ejemplo simple por compatibilidad, existe el `example` histórico, pero en FastAPI moderno es preferible pensar primero en `examples` u `openapi_examples`.

## 14. Cuándo usar `include_in_schema`

- Úsalo para ocultar una ruta o un parámetro de la documentación OpenAPI generada.
- Es útil en rutas internas, experimentales, de transición o en parámetros de depuración que no quieres enseñar.
- No lo uses como mecanismo de seguridad.
- Si quieres ocultar toda la documentación en un entorno, normalmente es mejor desactivar OpenAPI o las URLs de docs con configuración de la app.

## 15. Cuándo usar `before` y `after` validators

- Usa `before` cuando necesites normalizar la entrada antes de que Pydantic la interprete.
- Es útil para aceptar formatos flexibles, datos heredados o valores "sucios" que quieres convertir.
- En validadores de modelo, `mode="before"` sirve para preprocesar el diccionario crudo antes de construir el modelo.
- Usa `after` cuando el valor ya está validado y solo quieres comprobar invariantes, relaciones o transformaciones seguras.
- En validadores de modelo, `mode="after"` es ideal para revisar coherencia entre campos una vez creado el objeto.
- `after` suele ser más simple y más seguro porque ya trabajas con tipos correctos.
- Evita `before` en campos discriminadores de un `Union` discriminado, porque puede romper la selección del tipo correcto.

Regla rápida:

- `before` = "limpiar y adaptar entrada cruda".
- `after` = "verificar o ajustar después de validar tipos".

## 16. Orden de parámetros y uso de `*`

- Python exige que los parámetros sin valor por defecto vayan antes que los que sí tienen valor por defecto.
- FastAPI identifica los parámetros por nombre, tipo y marcador (`Query`, `Path`, `Body`, etc.), no por el orden.
- Si necesitas ordenar la firma de forma más flexible en estilo no `Annotated`, puedes usar `*` para forzar parámetros solo por palabra clave.
- En FastAPI moderno, `Annotated` reduce bastante la necesidad de trucos con el orden.

Ejemplo:

```python
async def read_items(*, item_id: int = Path(...), q: str):
    ...
```

## 17. Cuándo usar un modelo Pydantic y cuándo un tipo "arbitrario"

- Usa un modelo Pydantic cuando el dato tiene estructura clara, varios campos, validaciones propias y quieres reutilizarlo.
- Usa un tipo concreto o genérico cuando el payload es naturalmente una lista, un diccionario o un valor simple.
- Usa `UUID`, `datetime`, `Decimal`, `Enum`, `HttpUrl`, `EmailStr` y tipos parecidos cuando describen mejor el dato que un `str` genérico.
- Si el objeto no es JSON-friendly o no tiene forma clara de esquema, normalmente conviene modelarlo antes de exponerlo por la API.
- En FastAPI, muchas veces la mejor respuesta es: "modelo para la forma pública del recurso; tipos genéricos para colecciones y valores puntuales".

## 18. Framework, ORM y herramientas de migración

- Un framework web se encarga del ciclo de petición/respuesta, rutas, dependencias, middleware y serialización.
- Un ORM se encarga de mapear objetos de Python a tablas y filas, y de facilitar consultas y persistencia.
- Una herramienta de migraciones versiona cambios del esquema de la base de datos y permite aplicarlos y deshacerlos de forma controlada.
- FastAPI no sustituye al ORM ni a las migraciones.
- Lo típico es combinar las tres piezas: FastAPI + ORM + migraciones.

Ejemplos mentales:

- Framework: FastAPI.
- ORM: SQLAlchemy o SQLModel.
- Migraciones: Alembic.

## 19. Qué es una importación circular

- Ocurre cuando dos módulos se importan entre sí, directa o indirectamente.
- Python empieza a cargar un módulo y, antes de terminar, intenta cargar el otro, que vuelve a pedir algo del primero.
- El resultado típico es un error de "partially initialized module" o un `ImportError` similar.
- En FastAPI pasa mucho cuando `main.py` importa `routers.py` y `routers.py` vuelve a importar `main.py`.
- La solución suele ser mover código compartido a otro módulo, retrasar imports hasta dentro de funciones o cambiar la dirección de las dependencias.

Regla práctica: evita que tus routers, modelos y dependencias importen el `app` principal.

## 20. Reglas rápidas para recordar

- Si el dato identifica el recurso, va en la ruta.
- Si el dato filtra o modifica la consulta, va en query.
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
