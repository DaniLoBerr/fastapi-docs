"""17/111 - Extra Data Types
https://fastapi.tiangolo.com/tutorial/extra-data-types/
"""

from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/user-guide/extra-data-types", tags=["Tutorial Básico de FastAPI"]
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Tutorial Básico de FastAPI",
        "lesson": "Extra Data Types",
        "path": "/user-guide/extra-data-types",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/extra-data-types/",
    }


# EXTRA DATA TYPES
#   UUID
#   datetime.datetime
#   datetime.date
#   datetime.time
#   datetime.timedelta
#   frozenset
#   bytes
#   Decimal

from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID


@router.put("/extra-data-types/{item_id}")
async def extra_data_types(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time, Body()],
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
