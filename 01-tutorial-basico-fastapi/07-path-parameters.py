"""7/111 - Path Parameters
https://fastapi.tiangolo.com/tutorial/path-params/
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/user-guide/path-parameters", tags=["Tutorial Básico de FastAPI"]
)

# Agrega aquí el código de la lección de FastAPI


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Path Parameters",
        "path": "/user-guide/path-parameters",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/path-params/",
    }


# Enums and path parameters
from enum import Enum


class SubjectName(str, Enum):
    software = "software-engineering"
    math = "introduction-to-mathematics"
    foundations = "foundations-of-programming"


@router.get("/subjects/{subject_name}")
async def get_subject_name(subject_name: SubjectName):
    MESSAGES: dict[SubjectName, str] = {
        SubjectName.software: "You'll learn about software development processes, requirements, and design",
        SubjectName.foundations: "You'll learn about programming concepts, data structures, and algorithms",
        SubjectName.math: "You'll learn about sets, functions, and relations",
    }

    return {"subject_name": subject_name.value, "message": MESSAGES[subject_name]}


# Paths in path parameters
@router.get("/exports/{file_path:path}")
async def get_file_path(file_path: str):
    if file_path.endswith(".csv"):
        return {"file_path": file_path, "message": "Exporting CSV file."}
    return {"message": "Invalid file type. Only CSV files are allowed."}
