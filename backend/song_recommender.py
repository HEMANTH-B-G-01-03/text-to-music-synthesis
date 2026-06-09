# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")

# API_URL = "https://router.huggingface.co/v1/chat/completions"

# HEADERS = {
#     "Authorization": f"Bearer {HF_TOKEN}",
#     "Content-Type": "application/json"
# }


# def recommend_songs(prompt):

#     payload = {
#         "model": "Qwen/Qwen2.5-7B-Instruct",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": """
# You are a music recommendation assistant.

# Given a music prompt, recommend exactly 3 real songs.

# Return only the song names and artists.

# Format:

# 1. Song Name - Artist

# 2. Song Name - Artist

# 3. Song Name - Artist
# """
#             },
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     }

#     response = requests.post(
#         API_URL,
#         headers=HEADERS,
#         json=payload
#     )

#     data = response.json()

#     return data["choices"][0]["message"]["content"]


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


def recommend_songs(prompt):

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": """
You are a music recommendation assistant.

Recommend exactly 3 REAL and well-known songs that match the user's music request.

Only recommend existing songs from real artists.

Return only:

1. Song Name - Artist
2. Song Name - Artist
3. Song Name - Artist

Do not add explanations.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload
    )

    data = response.json()

    songs_text = data["choices"][0]["message"]["content"]

    recommendations = []

    for line in songs_text.split("\n"):

        line = line.strip()

        if not line:
            continue

        line = line.lstrip("1234567890. ")

        recommendations.append({
            "title": line,
            "youtube_url":
                f"https://www.youtube.com/results?search_query={line.replace(' ', '+')}"
        })

    return recommendations