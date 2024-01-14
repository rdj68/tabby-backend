from fastapi import FastAPI
from controller import get_health_state
from dotenv import load_dotenv
from aiModelClient.geckoClient import GeckoClient
import schemas

app = FastAPI()
load_dotenv()
gecko_client = GeckoClient()


@app.post("/v1/completions")
async def completion(request_body: schemas.CompletionRequest):
    print("Completion request received")
    prefix = request_body.segments.get("prefix", None)
    suffix = request_body.segments.get("suffix", None)

    response = await gecko_client.prompt(prefix, suffix=suffix)
    completion_response = get_completion_response(response.text)
    return completion_response


@app.get("/v1/health", response_model=schemas.HealthState)
def read_health():
    health_state = get_health_state()
    return health_state


@app.post("/v1/events")
async def event(request_body: schemas.LogEventRequest):
    print(event)
    pass


def get_completion_response(text: str):
    choices = [{"index": 0, "text": text}]

    return schemas.CompletionResponse(id="123", choices=choices, debug_data=None)