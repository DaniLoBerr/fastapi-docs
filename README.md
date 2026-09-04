# FastAPI Tutorial — Learning Notebook

![Python](https://img.shields.io/badge/python-3.14%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138-05998b)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

A hands-on, endpoint-by-endpoint walk through the entire official FastAPI documentation — Foundations, Tutorial, Advanced User Guide, Deployment, and How-To Recipes — built as one living FastAPI app instead of a folder of throwaway scripts.

## 📌 What this is

This is step 1 of my personal roadmap to become a Backend Engineer. Instead of just reading the FastAPI docs, I turned them into a real, running application: every lesson in the official [Learn](https://fastapi.tiangolo.com/learn/) section becomes its own endpoint in this API.

It's a study notebook, not a production project — but it's still built the way a real FastAPI app would be: properly structured, linted, and documented.

## 🧠 How it works

Every page of the FastAPI docs gets its own lesson file. Each one:

- Declares an `APIRouter`, scoped to its section (e.g. *Tutorial - User Guide*, *Advanced User Guide*, *CLI, editor y despliegue*)
- Exposes a base endpoint returning the lesson's metadata and a direct link back to the exact page of the official docs it's based on
- Leaves a marked spot (`# Agrega aquí el código de la lección de FastAPI`) where I implement the actual concept being taught

`routers.py` keeps a registry of every section and lesson (title, slug, reference URL), `lesson_routers.py` collects each lesson's router, and `main.py` wires everything into a single app. `main.py` doubles as its own lesson, too — it registers several custom and overridden exception handlers, straight out of the docs' error-handling chapter.

Hit any endpoint and you get back exactly which lesson you're looking at and where to read more:

```json
{
  "section": "CLI, editor y despliegue",
  "lesson": "Run a Server Manually",
  "path": "/cli-editor-deployment/run-a-server-manually",
  "reference_url": "https://fastapi.tiangolo.com/deployment/manually/"
}
```

## 📂 Structure

```
fastapi-tutorial/
├── 01-tutorial-basico-fastapi/              # Foundations + core User Guide
│   ├── 05-tutorial-user-guide.py
│   ├── 06-first-steps.py
│   └── README.md                            # Recap notes (ES) for this section
├── 07-advanced-user-guide-respuestas-dependencias/
│   └── 56-advanced-user-guide.py
├── 12-cli-editor-despliegue/                # Deployment section
│   ├── 96-run-a-server-manually.py
│   └── 99-server-workers-uvicorn-with-workers.py
├── routers.py                               # Section/lesson registry
├── lesson_routers.py                        # Collects every lesson's router
├── errors.py                                # Custom exceptions (e.g. UnicornError)
├── main.py                                  # App entrypoint + exception-handling playground
├── resumen-dudas-fastapi.md                 # Running FAQ / concept notes (ES)
└── pyproject.toml
```

Each numbered folder mirrors a section of the official docs, in the order I'm working through them. Every lesson file carries its position within the official Learn section (e.g. lesson 56, 96, 99...), so I always know exactly where I am without checking anything else.

## 🚀 Running it

```bash
uv sync
uv run fastapi dev
```

Then open:

- `http://127.0.0.1:8000` — welcome endpoint
- `http://127.0.0.1:8000/docs` — interactive Swagger UI, auto-listing every lesson endpoint built so far
- `http://127.0.0.1:8000/redoc` — alternative API docs

Without `uv`:

```bash
uvicorn main:app --reload
```

## 🧩 Code quality

Even a learning repo gets linted properly. Ruff runs with a strict rule set — type annotations (`ANN`), async correctness (`ASYNC`), basic security checks (`S`), bugbear (`B`), simplification (`SIM`) — because good habits shouldn't wait for a "real" project to start.

## 📖 Notes & recaps

Study notes live alongside the code, not in a separate wiki:

- Every completed section gets its own recap README (in Spanish) — mental models, gotchas, and a short summary of the core ideas.
- `resumen-dudas-fastapi.md` is a running log of the things I had to stop and actually think through: `async`/`await`, environment variables, how `uv` manages the project, how a request really flows through the ASGI stack, and more.

## 🗺️ Context

This repo is step 1 of my roadmap to become a Backend Engineer — you can check out the full plan on my [GitHub profile](https://github.com/DaniLoBerr).

## 📈 Status

🔄 In progress — currently working through the FastAPI Learn section end to end: Foundations → Tutorial → Advanced User Guide → Deployment → How-To Recipes.
