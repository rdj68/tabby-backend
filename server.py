from fastapi import FastAPI, Body, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from controller import get_health_state, create_prompt
from dotenv import load_dotenv
from aiModelClient.geckoClient import GeckoClient
import schemas

app = FastAPI()
load_dotenv()
geckoClient = GeckoClient()


@app.post("/v1/completions")
async def completion(request_body: schemas.CompletionRequest):

    print("completion request recieved ")
    prefix = request_body.segments.get(
        "prefix") if request_body.segments is not None else None
    suffix = request_body.segments.get(
        "suffix") if request_body.segments is not None else None

    response = await geckoClient.prompt(prefix, suffix=suffix)
    completion_response = get_completion_response(response.text)
    return completion_response


@app.get("/v1/health", response_model=schemas.HealthState)
def read_health():
    # Replace this with your function to get the health state
    health_state = get_health_state()
    return health_state


# class SearchResponse(BaseModel):
#     num_hits: int
#     hits: List[dict]

# @app.get("/v1beta/search")
# async def search(q: str = Query(...), limit: Optional[int] = 20, offset: Optional[int] = 0):
#     # Your code here
#     pass


@app.post("/v1/events")
async def event(request_body: schemas.LogEventRequest):
    print(event)
    pass

# function to get completion response from text


def get_completion_response(text: str):
    choices = []
    choices.append({
        "index": 0,
        "text": text
    })

    completion_response = schemas.CompletionResponse(
        id="123",
        choices=choices,
        debug_data=None
    )

    return completion_response
