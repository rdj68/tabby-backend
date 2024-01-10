from fastapi import FastAPI, Body, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from controller import get_health_state, create_prompt
import asyncio
import geminiClient
import schemas
import time 

app = FastAPI()


@app.post("/v1/completions")
async def completion(request_body: schemas.CompletionRequest):
    
    prompt = create_prompt(request_body)
    print("completion request recieved ")
    
    response = await geminiClient.prompt_gemini(prompt)
    completion_response = get_completion_response(response.text)
    print("completion response sent")
    return completion_response
    

@app.get("/v1/health", response_model=schemas.HealthState)
def read_health():
    health_state = get_health_state()  # Replace this with your function to get the health state
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
    choicesList = text.split("|||")
    for i in range(len(choicesList)):
    
        choices.append({
            "index": i,
            "text": choicesList[i]
        })
        
    completion_response =  schemas.CompletionResponse(
        id="123",
        choices= choices,
        debug_data=None
    )

    return completion_response