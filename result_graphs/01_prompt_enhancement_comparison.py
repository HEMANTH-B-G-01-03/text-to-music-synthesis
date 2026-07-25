import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

prompts = [
    "Happy flute music",
    "Calm piano melody",
    "Energetic rock music",
    "Relaxing guitar music",
    "Lo-fi study music"
]


def enhance_prompt(prompt):
    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert music prompt engineer. "
                    "Expand the user's prompt with musical attributes like mood, tempo, "
                    "genre, rhythm and instruments."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]


original_counts = []
enhanced_counts = []

print("\nGenerating enhanced prompts...\n")

for prompt in prompts:
    enhanced = enhance_prompt(prompt)

    original_counts.append(len(prompt.split()))
    enhanced_counts.append(len(enhanced.split()))

    print("--------------------------------------")
    print("Original :", prompt)
    print("Enhanced :", enhanced)
    print("--------------------------------------")

plt.figure(figsize=(10,6))

x = range(len(prompts))
width = 0.35

plt.bar(
    [i-width/2 for i in x],
    original_counts,
    width,
    label="Original Prompt"
)

plt.bar(
    [i+width/2 for i in x],
    enhanced_counts,
    width,
    label="Enhanced Prompt"
)

plt.xticks(x, prompts, rotation=15)
plt.ylabel("Number of Words")
plt.xlabel("Input Prompt")
plt.title("Prompt Enhancement Comparison")
plt.legend()

plt.tight_layout()

os.makedirs("result_graphs", exist_ok=True)

plt.savefig(
    "result_graphs/prompt_enhancement_comparison.png",
    dpi=300
)

plt.show()

print("\nGraph saved successfully!")