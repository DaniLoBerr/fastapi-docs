# FastAPI — Documentation Study Notebook

Working through the **entire official FastAPI documentation** as one coherent application instead of scattered practice scripts. Every page of the docs gets its own lesson file, its own router, and its own notes.

![Status](https://img.shields.io/badge/status-in%20progress-brightgreen)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688)
![Ruff](https://img.shields.io/badge/linting-ruff%20strict-orange)

---

## 📍 Status

> **🟢 In progress.** This is the first step of my [backend engineering roadmap](https://github.com/DaniLoBerr) and it is actively being worked on. Lessons are committed as I complete each section of the official docs.

---

## 🎯 What this is and why it exists

Most people "learn FastAPI" by following a tutorial once and then forgetting where anything was. This repo is the opposite approach: a **single running application** that grows one endpoint per documentation lesson, so the whole framework ends up navigable, executable and annotated in one place.

It also serves a second purpose, which matters more to me: it's where I prove that **good habits don't wait for a "real" project**. Strict linting, type annotations, consistent structure and written notes are applied here exactly as they would be in production code.

## 🧱 How it's organised

Numbered folders mirror the official *Learn* section, so any lesson can be traced back to its source page:

```
Foundations → Tutorial – User Guide → Advanced User Guide → Deployment
```

Each lesson file contains:

- An `APIRouter` scoped to its documentation section
- A base endpoint returning the lesson metadata and a link to the official source
- The implementation of the concept being studied
- Notes on anything that needed a second read

Routers are wired through a registry, so adding a lesson never means touching the app entry point.

## 🧹 Code quality

Linted with **Ruff** under a strict rule set: type annotations, `async` correctness, security checks and import hygiene. A study repo is exactly where those habits should be built, not where they should be skipped.

## 📚 Notes

Study notes live inside the codebase rather than in a separate wiki:

- Section-level READMEs explaining what that part of the docs covers
- A running **FAQ file** with the concepts that took real thinking — dependency injection resolution order, `async` vs `def` in path operations, response model filtering, and the security chapter in particular

## 🏁 Running it

```bash
# With uv (recommended)
uv sync
uv run fastapi dev

# Or with plain uvicorn
uvicorn main:app --reload
```

Interactive docs at `http://localhost:8000/docs` — where, appropriately, you can browse the lessons through the very feature being studied.

## 🗺️ Context

This is **step 1** of a structured roadmap from QA engineering to backend development. The next steps build on it: test-driven development with Docker and CI, then test automation, then three projects of increasing architectural complexity.

👉 Full roadmap and project list on my **[GitHub profile](https://github.com/DaniLoBerr)**.
