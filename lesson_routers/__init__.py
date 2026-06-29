import importlib.util
from pathlib import Path

from fastapi import APIRouter

lesson_routers = []
project_root = Path(__file__).resolve().parent.parent

for lesson_dir in sorted(project_root.iterdir()):
    if not lesson_dir.is_dir() or not lesson_dir.name[0].isdigit():
        continue

    for lesson_file in sorted(lesson_dir.glob("*.py")):
        if lesson_file.name.startswith("_"):
            continue

        module_name = f"lesson_routers.{lesson_dir.name}.{lesson_file.stem}"
        spec = importlib.util.spec_from_file_location(module_name, lesson_file)
        if spec is None or spec.loader is None:
            continue

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        router = getattr(module, "router", None)
        if isinstance(router, APIRouter):
            lesson_routers.append(router)
