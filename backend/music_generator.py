# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")

# API_URL = "https://router.huggingface.co/fal-ai/fal-ai/musicgen-small"

# HEADERS = {
#     "Authorization": f"Bearer {HF_TOKEN}",
#     "Content-Type": "application/json"
# }


# def generate_music(prompt):

#     payload = {
#         "prompt": prompt
#     }

#     response = requests.post(
#         API_URL,
#         headers=HEADERS,
#         json=payload
#     )

#     print(response.status_code)
#     print(response.text)

#     return response.json()


from transformers import pipeline
import scipy
import uuid
import os

print("Loading MusicGen...")

pipe = pipeline(
    "text-to-audio",
    model="facebook/musicgen-small",
    device=-1
)

print("MusicGen loaded successfully!")


def generate_music(prompt):

    os.makedirs("outputs", exist_ok=True)

    music = pipe(
        prompt,
        forward_params={
            "max_new_tokens":  1024
        }
    )

    filename = f"{uuid.uuid4()}.wav"
    filepath = os.path.join("outputs", filename)

    scipy.io.wavfile.write(
        filepath,
        rate=music["sampling_rate"],
        data=music["audio"]
    )

    return filepath