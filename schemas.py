from pydantic import BaseModel, Field
from typing import List, Optional

# completion api request and response
class CompletionRequest(BaseModel):
    language: Optional[str] = None
    segments: Optional[dict] = None
    user: Optional[str] = None
    debug_options: Optional[dict] = None

class CompletionResponse(BaseModel):
    id: str
    choices: List[dict]
    debug_data: Optional[dict] = None


# Health api response
class Version(BaseModel):
    build_date: str
    build_timestamp: str
    
    git_sha: str
    git_describe: str

class HealthState(BaseModel):
    model: str
    chat_model: str = Field(None)
    device: str
    arch: str
    cpu_info: str
    cpu_count: int
    cuda_devices: List[str]
    version: Version

class LogEventRequest(BaseModel):
    type: str
    completion_id: str
    choice_index: int