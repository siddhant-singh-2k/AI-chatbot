
from pydantic import  BaseModel
from ai_agent import get_response_from_agent
from typing import List


class RequestState (BaseModel):
    model_name : str
    model_provider : str
    system_prompt: str
    messages: List[str]
    allow_search: bool


from fastapi import  FastAPI

ALLOWED_MODELS_NAME = ["gpt-4o-mini","llama-3.3-70b-versatile"]

app = FastAPI(title="AI Agent")

@app.post('/chat')

def chat_endpoint (request:RequestState):
    """
    API Endpoint to chat with the created model
    """
    if request.model_name not in ALLOWED_MODELS_NAME:
        return {"error","Invalid model name"}

    llm_id = request.model_name
    query = request.messages
    allowed_search  = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    response = get_response_from_agent(llm_id,query,allowed_search,system_prompt,provider)
    return  response

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host = "127.0.0.1" , port  = 9999)


