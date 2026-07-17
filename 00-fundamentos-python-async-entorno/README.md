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

FastAPI aprovecha el modelo asíncrono de Python para maximizar el rendimiento al manejar muchas peticiones I/O-bound (bases de datos, llamadas HTTP, etc.).

Reglas prácticas:

- Si llamas a librerías **asíncronas** (que requieren `await`), tu función de path debe ser `async def`, y dentro usarás `await` para las operaciones I/O.
- Si usas librerías **bloqueantes** (no soportan `await`), define la función del path como `def` normal; FastAPI la ejecutará en un threadpool para no bloquear el servidor.
- Puedes mezclar `def` y `async def` en diferentes endpoints y dependencias; FastAPI se encarga de integrarlo de forma eficiente.
- La regla general del tutorial: *si sabes que necesitas `await`, usa `async def`; si no estás seguro, empieza con `def`*.

La idea es que mientras una petición espera I/O, el servidor puede seguir atendiendo otras, lo que da un rendimiento muy alto especialmente bajo carga.

## 3. Variables de entorno

Las variables de entorno permiten configurar tu aplicación sin hardcodear datos sensibles o específicos del entorno (desarrollo, staging, producción) en el código.

Conceptos clave:

- Una variable de entorno se define en el sistema operativo (por ejemplo, `export MY_NAME="Wade Wilson"` en Linux/macOS o `$Env:MY_NAME = "Wade Wilson"` en PowerShell).
- Desde Python las lees con `os.getenv("NOMBRE", "valor_por_defecto")`; todo lo que viene de entorno es `str`, así que cualquier conversión la haces tú o la delegas a una clase de settings.
- Es habitual usar variables de entorno para: claves API, cadenas de conexión a BD, flags de entorno (`ENV=dev|prod`), URLs de servicios externos, etc.
- La variable especial `PATH` define dónde busca el sistema los ejecutables (incluido `python`), y se ve afectada por cómo instalas Python y cómo activas entornos virtuales.

Usar variables de entorno te permite desplegar la misma imagen de aplicación en distintos entornos cambiando solo la configuración externa.

## 4. Entornos virtuales (`venv`)

Un entorno virtual es una instalación aislada de Python (y sus paquetes) dentro de una carpeta de tu proyecto, de forma que cada proyecto tiene sus propias dependencias sin interferir con otros.

Flujo típico:

1. **Crear el entorno virtual** dentro del proyecto:

   ```bash
   python -m venv .venv
   ```

   Esto crea la carpeta `.venv/` con un intérprete de Python y `pip` independientes.

2. **Activar el entorno**:

   - Linux/macOS:

     ```bash
     source .venv/bin/activate
     ```

   - Windows PowerShell:

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

   Al activar, se modifica `PATH` para que `python` y `pip` apunten al entorno virtual.

3. **Actualizar `pip` e instalar dependencias** (como FastAPI):

   ```bash
   python -m pip install --upgrade pip
   pip install "fastapi[standard]"
   ```

   Estas dependencias se instalan solo en ese proyecto.

4. **Ignorar `.venv` en el control de versiones** y compartir solo `requirements.txt` o `pyproject.toml`, para que otros puedan recrear el entorno.

Beneficios: evitas conflictos de versiones entre proyectos, facilitas reproducibilidad (incluyendo CI/CD) y mantienes limpio el Python global.

## 5. Cómo encaja todo en tu flujo de trabajo

- **Tipos de Python + Pydantic** → describes tus datos una sola vez y obtienes validación, conversión y documentación automática en FastAPI.
- **Concurrencia con `async/await`** → eliges `async def` cuando consumes librerías asíncronas y `def` cuando usas librerías bloqueantes, manteniendo el servidor eficiente.
- **Variables de entorno** → mantienes la configuración sensible y dependiente del entorno fuera del código, lo que facilita despliegues en distintos entornos.
- **Entornos virtuales** → cada proyecto FastAPI tiene su propio Python y dependencias, evitando el "dependency hell" y asegurando entornos reproducibles.
