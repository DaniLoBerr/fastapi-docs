"""22/111 - Response Model - Return Type
https://fastapi.tiangolo.com/tutorial/response-model/
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/special-params/response-model-return-type",
    tags=["Parámetros especiales, modelos en capas y respuestas"],
)


@router.get("/")
async def read_lesson():
    return {
        "section": "Parámetros especiales, modelos en capas y respuestas",
        "lesson": "Response Model - Return Type",
        "path": "/special-params/response-model-return-type",
        "reference_url": "https://fastapi.tiangolo.com/tutorial/response-model/",
    }


# Response Model - Return Type
# response_model parameter
#   Return some data that it's not exactly what the type declares
#   Example: return a dict but declare it as a Pydantic model

# response_model priority
# return the same input data
# add an output model
# response model or return type
# return type and data filtering
# type annotations and tooling
# fastapi data filtering
# other return type annotations
# return a response directly
# annotate a response subclass
# Invalid Return Type Annotations
# disable response model
# Response Model encoding parameters
# Use the response_model_exclude_unset parameter
# Data with values for fields with defaults
# Data with the same values as the defaults
# response_model_include and response_model_exclude
# Using lists instead of sets
