import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/fal-ai/fal-ai/musicgen-small"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def generate_music(prompt):

    payload = {
        "prompt": prompt
    }

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload
    )

    print(response.status_code)
    print(response.text)

    return response.json()