# Resumen de fundamentos de Python, async y entorno en FastAPI

Este README resume las primeras lecciones del tutorial de FastAPI sobre tipos de Python, concurrencia `async/await`, variables de entorno y entornos virtuales.

## 1. Tipos de Python y FastAPI

FastAPI se apoya fuertemente en las anotaciones de tipo de Python para darte validación, conversión automática de datos y documentación OpenAPI, además de mejor autocompletado en el editor.

Puntos clave:

- Las anotaciones de tipo (`name: str`, `age: int`, etc.) no cambian el comportamiento en tiempo de ejecución, pero ayudan al editor a detectar errores y ofrecer autocompletado.
- Puedes tipar tipos simples (`int`, `float`, `bool`, `bytes`) y tipos genéricos como `list[str]`, `tuple[int, int]`, `set[bytes]`, `dict[str, float]` para describir mejor tus estructuras.
- Las uniones (`int | str`) y los tipos opcionales (`str | None`) expresan parámetros que aceptan múltiples tipos o pueden ser `None`, y el editor puede avisarte si olvidas tratarlos.
- Los modelos de Pydantic (`class User(BaseModel): ...`) combinan tipos + validación/conversión; FastAPI los usa para validar automáticamente el cuerpo de las peticiones y generar la documentación.

En resumen: define siempre tipos en parámetros, respuestas y modelos; FastAPI hace el trabajo pesado de validación y documentación por ti.

## 2. Concurrencia y async/await

FastAPI aprovecha el modelo asíncrono de Python para maximizar el rendimiento al manejar muchas peticiones simultáneamente, especialmente en operaciones I/O-bound.

### Conceptos clave

**Asincronía e I/O-bound**: Código asincrónico permite al programa avisar que, en cierto punto, debe esperar algo externo (base de datos, llamada HTTP, lectura de archivo, etc.). Mientras espera, el servidor puede procesar otras peticiones en lugar de quedarse bloqueado. Esto es especialmente valioso en aplicaciones web, donde hay muchos usuarios con conexiones "lentas", y el servidor pasa la mayor parte del tiempo esperando I/O.

**Concurrencia vs. Paralelismo**: Son conceptos diferentes:
- **Concurrencia**: Múltiples tareas haciendo "más o menos" algo al mismo tiempo, pero el procesador solo ejecuta una a la vez. Cuando una se pausa (esperando I/O), el procesador puede cambiar a otra. Es ideal para operaciones I/O-bound.
- **Paralelismo**: Múltiples tareas ejecutándose realmente en paralelo en diferentes procesadores. Es ideal para operaciones CPU-bound (procesamiento de imagen, Machine Learning, cálculos intensivos).

**async/await en Python**: Sintaxis moderna y legible para escribir código asincrónico:
- `async def` declara una función como corrutina (puede ser pausada/reanudada).
- `await` pausa la ejecución actual y espera a que termine algo async. Solo funciona dentro de `async def`.
- Una corrutina es el objeto que produce una función `async def`; representa una tarea que puede quedar "en pausa" y retomarse después.

### Reglas prácticas

- **Con librerías asincrónas** (que requieren `await`): Define tu función de path con `async def` y usa `await` para las operaciones.
  
  ```python
  @app.get("/items/")
  async def read_items():
      results = await some_async_library()
      return results
  ```

- **Con librerías bloqueantes** (no soportan `await`): Usa `def` normal; FastAPI la ejecutará en un threadpool para no bloquear el servidor.
  
  ```python
  @app.get("/items/")
  def read_items():
      results = some_blocking_library()
      return results
  ```

- **Cuando dudes**: Usa `def` normal. Si luego necesitas cambiar a asincrónico, lo modificas.

- **Puedes mezclar**: Endpoints, dependencias y sub-dependencias pueden ser `def` o `async def`; FastAPI se encarga de integrarlos eficientemente.

### Detalles técnicos

FastAPI hace una distinción técnica importante entre funciones normales y corrutinas.

Cuando FastAPI ve una función `def`:
- La ejecuta en un **threadpool externo** para no bloquear el servidor.
- Esto permite que operaciones bloqueantes (como consultas a BD síncronas) no cuelguen la aplicación.

Cuando FastAPI ve una función `async def`:
- La ejecuta directamente en el **event loop** de manera concurrente.
- Es más eficiente si la librería es verdaderamente async.

En FastAPI la misma regla se aplica a las dependencias y sub-dependencias:
- Una dependencia `def` se ejecuta en el threadpool.
- Una dependencia `async def` se ejecuta en el event loop.
- Puedes mezclar dependencias `def` y `async def` y FastAPI gestionará la llamada correcta.

También hay un matiz importante en la lección: si vienes de otros frameworks asíncronos y quieres usar `def` en funciones de path solo por un pequeño ahorro de CPU, en FastAPI eso no es la mejor opción. Aquí, `async def` suele ser preferible salvo que el código real sea bloqueante.

Finalmente, las utilidades normales que llamas desde tu código no las gestiona FastAPI internamente. Si son `def`, se llaman directamente; si son `async def`, debes `await`arlas tú mismo.

En resumen: mientras una petición espera externo (I/O), el servidor puede atender otras. Esto proporciona rendimiento excepcional bajo carga, especialmente combinado con la capacidad de FastAPI de usar multiples workers en producción (paralelismo adicional).

## 3. Variables de entorno

Las variables de entorno permiten configurar tu aplicación sin hardcodear datos sensibles o específicos del entorno (desarrollo, staging, producción) en el código.

Conceptos clave:

- Una variable de entorno se define en el sistema operativo (por ejemplo, `export MY_NAME="Wade Wilson"` en Linux/macOS o `$Env:MY_NAME = "Wade Wilson"` en PowerShell).
- Desde Python las lees con `os.getenv("NOMBRE", "valor_por_defecto")`; todo lo que viene de entorno es `str`, así que cualquier conversión la haces tú o la delegas a una clase de settings.
- Es habitual usar variables de entorno para: claves API, cadenas de conexión a BD, flags de entorno (`ENV=dev|prod`), URLs de servicios externos, etc.
- La variable especial `PATH` define dónde busca el sistema los ejecutables (incluido `python`), y se ve afectada por cómo instalas Python y cómo activas entornos virtuales.

Usar variables de entorno te permite desplegar la misma imagen de aplicación en distintos entornos cambiando solo la configuración externa.

## 4. Entornos virtuales (`uv`)

En Linux, lo más cómodo para gestionar entornos virtuales y paquetes es usar `uv` como herramienta principal.

### Por qué usar `uv`

`uv` puede crear el entorno virtual, instalar paquetes y bloquear dependencias de forma más integrada que `pip`/`venv` por separado. Si ya conoces `uv`, te simplifica el flujo de trabajo y evita tener que preocuparte de actualizar `pip` manualmente.

### Crear y activar el entorno con `uv`

Dentro del directorio de tu proyecto, puedes crear/gestionar el entorno con:

```bash
uv init
```

Eso crea un entorno aislado para tu proyecto y, si lo deseas, un archivo de dependencias.

Para activar el entorno con `uv`, normalmente puedes usar el shell de tu sistema después de iniciar el proyecto. En Linux, si `uv` genera un entorno `.venv`, úsalo así:

```bash
source .venv/bin/activate
```

### Instalar paquetes con `uv`

Usa `uv` para instalar FastAPI y otras dependencias:

```bash
uv install "fastapi[standard]"
```

Esto instala los paquetes en el entorno del proyecto sin necesidad de ejecutar `python -m pip install`.

### Verificar el entorno

Comprueba que `python` apunta al entorno del proyecto:

```bash
which python
```

Debe devolver una ruta dentro de `.venv/bin/`.

### `.gitignore` y versiones de dependencias

`uv` suele crear un `.gitignore` adecuado automáticamente, y te ayuda a mantener un archivo de lock con versiones exactas.

### Alternativa si no usas `uv`

Si no usas `uv`, el flujo tradicional en Linux es:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install "fastapi[standard]"
```

Pero en este resumen, el enfoque recomendado es usar `uv` cuando sea posible.

### Ejecutar tu aplicación

Con el entorno activo, ejecuta tu aplicación desde el entorno:

```bash
python main.py
```

O bien, utiliza los comandos de `uv` para gestionar y ejecutar tu proyecto según tu configuración.

Beneficios: con `uv` evitas gran parte de la gestión manual de entornos y paquetes, y mantienes cada proyecto aislado sin mezclar dependencias globales.

## 5. Cómo encaja todo en tu flujo de trabajo

- **Tipos de Python + Pydantic** → describes tus datos una sola vez y obtienes validación, conversión y documentación automática en FastAPI.
- **Concurrencia con `async/await`** → eliges `async def` cuando consumes librerías asíncronas y `def` cuando usas librerías bloqueantes, manteniendo el servidor eficiente.
- **Variables de entorno** → mantienes la configuración sensible y dependiente del entorno fuera del código, lo que facilita despliegues en distintos entornos.
- **Entornos virtuales** → cada proyecto FastAPI tiene su propio Python y dependencias, evitando el "dependency hell" y asegurando entornos reproducibles.
