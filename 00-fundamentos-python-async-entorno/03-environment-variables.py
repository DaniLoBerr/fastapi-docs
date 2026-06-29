"""3/111 - Environment Variables
https://fastapi.tiangolo.com/environment-variables/
"""

from os import environ

from fastapi import APIRouter
from pydantic import BaseModel


class EnvVariable(BaseModel):
    name: str
    value: str


router = APIRouter(
    prefix="/foundations/environment-variables",
    tags=["Fundamentos de Python, async y entorno"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Fundamentos de Python, async y entorno",
        "lesson": "Environment Variables",
        "path": "/foundations/environment-variables",
        "reference_url": "https://fastapi.tiangolo.com/environment-variables/",
    }


@router.get("/get-envs")
async def get_envs():
    return {"environment_variables": dict(environ)}


@router.get("/env/{variable_name}")
async def get_env_variable_by_name(variable_name: str):
    var: str = variable_name.upper()
    value: str | None = environ.get(var)
    if value is None:
        return {"error": f"Environment variable '{var}' not found."}
    return {var: value}


@router.post("/set-env")
async def set_env_variable(env_var: EnvVariable):
    data: dict = {env_var.name.upper(): env_var.value}
    environ.update(data)
    return {
        "message": f"Environment variable '{env_var.name.upper()}' set to '{env_var.value}'."
    }
