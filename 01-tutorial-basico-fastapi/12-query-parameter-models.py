"""12/111 - Query Parameter Models
https://fastapi.tiangolo.com/tutorial/query-param-models/
"""

from typing import Annotated, Literal

from fastapi import APIRouter, Query
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/user-guide/query-parameter-models", tags=["Tutorial Básico de FastAPI"]
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Query Parameter Models",
        "path": "/user-guide/query-parameter-models",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/query-param-models/",
    }


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@router.get("/query-parameter-models")
async def query_parameter_models(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
