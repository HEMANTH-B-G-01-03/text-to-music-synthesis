from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

from fastapi.middleware.cors import CORSMiddleware

from backend.prompt_enhancer import enhance_prompt
from backend.music_generator import generate_music
from backend.song_recommender import recommend_songs

app = FastAPI()

app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

    # Enhance prompt
    enhanced_prompt = enhance_prompt(req.prompt)

    # Generate music
    audio_file = generate_music(enhanced_prompt)

    # Get song recommendations
    recommendations = recommend_songs(req.prompt)

    filename = os.path.basename(audio_file)

    return {
        "original_prompt": req.prompt,
        "enhanced_prompt": enhanced_prompt,
        "audio_url": f"/outputs/{filename}",
        "recommendations": recommendations
    }