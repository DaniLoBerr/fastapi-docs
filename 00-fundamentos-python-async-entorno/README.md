# Part 0 - Foundations

## Capítulo 1 - Python Types Intro

FastAPI se apoya en las anotaciones de tipos estándar de Python para validar datos, convertir valores automáticamente y generar documentación de la API.

La lección explica que los **type hints** de Python permiten indicar el tipo esperado de variables, parámetros y valores de retorno, como `str`, `int` o `bool`. Aunque Python no obliga a cumplirlos en tiempo de ejecución, estas anotaciones ayudan al editor, a los analizadores estáticos y a FastAPI a entender mejor el código.

### Tipos básicos

Se muestran ejemplos con tipos simples como `str`, `int`, `float`, `bool` y `bytes`. Al declarar una función con estos tipos, el editor puede ofrecer autocompletado y detectar posibles errores antes de ejecutar el programa.

### Tipos compuestos

La lección introduce contenedores tipados como `list[str]`, `tuple[int, int, str]`, `set[bytes]` y `dict[str, float]`. Esto permite describir no solo el tipo del contenedor, sino también el de sus elementos internos.

### Union y valores opcionales

También se explica cómo indicar que un valor puede tener más de un tipo, por ejemplo `int | str`. Para valores opcionales se usa `str | None`, lo que deja claro que una variable puede no tener contenido.

### Clases y Pydantic

La página muestra que las clases también pueden usarse como tipos, por ejemplo para indicar que un parámetro es una instancia de una clase concreta. Además, presenta modelos de Pydantic con `BaseModel`, donde los atributos tipados permiten validar y transformar datos automáticamente, algo central en FastAPI.

### Annotated

Por último, se menciona `Annotated`, una forma de adjuntar metadatos a un tipo sin cambiar el tipo principal. FastAPI puede aprovechar esa metadata para añadir validaciones o configuraciones extra sobre parámetros y datos.

## Capítulo 2 - Concurrency and async / await

La lección explica cuándo usar `async def` y cuándo usar `def` en FastAPI, además de la diferencia entre concurrencia y paralelismo.

### Regla rápida

- Usa `async def` si trabajas con librerías que se llaman con `await`.
- Usa `def` si la librería que usas hace I/O pero no soporta `await`.
- Si no tienes claro cuál usar, la documentación recomienda usar `def` normal.
- Puedes mezclar `def` y `async def` en la misma aplicación, y FastAPI gestionará ambos casos correctamente.

### Qué significa código asíncrono

El código asíncrono permite que el servidor no se quede bloqueado mientras espera operaciones lentas de I/O, como consultas a base de datos, llamadas a APIs externas, lectura de archivos o comunicación por red.
Mientras una tarea espera, el servidor puede atender otras peticiones.

### Concurrencia vs paralelismo

La documentación usa el ejemplo de las hamburguesas para explicar que la concurrencia es útil cuando hay mucho tiempo de espera, como ocurre en la mayoría de aplicaciones web.
En cambio, el paralelismo es más útil cuando el trabajo es principalmente de CPU, por ejemplo procesamiento de imágenes, audio o tareas de machine learning.

### Cómo funcionan `async` y `await`

- `await` se usa para esperar el resultado de una operación asíncrona sin bloquear el servidor.
- `await` solo puede usarse dentro de una función definida con `async def`.
- Una función `async def` devuelve una coroutine, que puede pausarse y reanudarse durante su ejecución.

### Qué hace FastAPI internamente

Si defines una ruta con `def` en vez de `async def`, FastAPI la ejecuta en un thread pool externo para evitar bloquear el servidor principal.
Ese mismo comportamiento también aplica a las dependencias y subdependencias definidas con `def`.

### Recomendación práctica

- Para operaciones de I/O no bloqueantes, usa `async def`.
- Para código bloqueante o librerías sin soporte async, usa `def`.
- Para tareas intensivas de CPU, piensa además en paralelismo o multiprocesamiento, no solo en async.

### Idea final

FastAPI aprovecha el modelo asíncrono de Python para ofrecer muy buen rendimiento en APIs web, especialmente en escenarios con mucha espera por I/O.

## Environment Variables

### Qué son

Las variables de entorno son valores que existen fuera del código Python, en el sistema operativo, y que la aplicación puede leer al ejecutarse.

### Para qué sirven

Se usan para guardar configuración, como claves, rutas o ajustes, sin escribir esos datos directamente en el código.

### Cómo se crean

En Unix/Linux/macOS se pueden definir con:

```bash
export MY_NAME="Wade Wilson"
```

En PowerShell se pueden definir con:

```powershell
$Env:MY_NAME = "Wade Wilson"
```

### Cómo leerlas en Python

Se leen con el módulo `os`:

```python
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name}")
```

### Valor por defecto

Si la variable no existe, `os.getenv()` puede devolver un valor por defecto en lugar de `None`.

### Uso temporal

También se puede definir una variable solo para una ejecución concreta:

```bash
MY_NAME="Wade Wilson" python main.py
```

### Importante

Todas las variables de entorno se leen como texto (`string`), así que si necesitas enteros, booleanos u otros tipos, debes convertirlos en Python.

### PATH

`PATH` es una variable de entorno especial que guarda las carpetas donde el sistema busca programas ejecutables como `python`.

## Virtual Environments

### Qué es un entorno virtual

- Es una carpeta que contiene su propio intérprete de Python y sus dependencias instaladas de forma aislada.
- Permite separar las librerías de un proyecto de las del sistema o de otros proyectos.

### Por qué usarlo

- Evita conflictos de versiones entre proyectos distintos.
- Hace más fácil mantener un entorno limpio y reproducible para desarrollar con FastAPI.

### Cómo crearlo

- Se usa el módulo integrado `venv` de Python con un comando como `python -m venv .venv`.
- Normalmente se recomienda crear el entorno dentro del proyecto con el nombre `.venv`.

### Cómo activarlo

- En Linux y macOS, suele activarse con `source .venv/bin/activate`.
- En Windows, suele activarse con `.venv\Scripts\activate`.

### Idea clave

- Una vez activado el entorno virtual, los comandos de `python` y `pip` trabajan dentro de ese entorno, no sobre la instalación global del sistema.
