"""2/111 - Concurrency and async / await
https://fastapi.tiangolo.com/async/
"""

from fastapi import APIRouter
from asyncio import sleep

router = APIRouter(prefix="/foundations/concurrency-and-async-await", tags=["Fundamentos de Python, async y entorno"])

@router.get("/async-await")
async def hey():
    print("Hey")
    await sleep(1)  # Simulate an async operation
    print("Hey after 1 second")
    return {"data": "Hey"}

