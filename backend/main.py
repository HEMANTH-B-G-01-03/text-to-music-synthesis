# from fastapi import FastAPI
# from pydantic import BaseModel

# from backend.prompt_enhancer import enhance_prompt

# app = FastAPI()


# class PromptRequest(BaseModel):
#     prompt: str


# @app.get("/")
# def home():
#     return {
#         "project": "Text To Music Synthesis",
#         "status": "running"
#     }


# @app.post("/enhance")
# def enhance(req: PromptRequest):

#     enhanced = enhance_prompt(req.prompt)

#     return {
#         "original_prompt": req.prompt,
#         "enhanced_prompt": enhanced
#     }


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

from backend.prompt_enhancer import enhance_prompt
from backend.music_generator import generate_music

app = FastAPI()
app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "project": "Text To Music Synthesis",
        "status": "running"
    }


@app.post("/generate")
def generate(req: PromptRequest):

    enhanced_prompt = enhance_prompt(req.prompt)

    audio_file = generate_music(enhanced_prompt)

    filename = os.path.basename(audio_file)

    return {
        "original_prompt": req.prompt,
        "enhanced_prompt": enhanced_prompt,
        "audio_url": f"/outputs/{filename}"
    }