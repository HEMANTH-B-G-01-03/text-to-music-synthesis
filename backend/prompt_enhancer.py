import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def enhance_prompt(user_prompt):

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": """
You are a music prompt engineer.

Convert simple user music requests into detailed prompts.

Include:
- instruments
- tempo
- mood
- rhythm
- genre

Return only the enhanced prompt.
"""
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    }

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]