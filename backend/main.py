from fastapi import FastAPI
from pydantic import BaseModel

from backend.prompt_enhancer import enhance_prompt

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "project": "Text To Music Synthesis",
        "status": "running"
    }


@app.post("/enhance")
def enhance(req: PromptRequest):

    enhanced = enhance_prompt(req.prompt)

    return {
        "original_prompt": req.prompt,
        "enhanced_prompt": enhanced
    }