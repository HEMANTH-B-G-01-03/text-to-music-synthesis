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

PROMPTS = [
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
                    "Expand the user's music prompt with mood, genre, "
                    "tempo, instruments and atmosphere. "
                    "Return only the enhanced prompt."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "temperature": 0.7,
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        print(response.text)
        raise Exception("API Error")

    return response.json()["choices"][0]["message"]["content"]


original_words = []
enhanced_words = []

print("\nGenerating enhanced prompts...\n")

for prompt in PROMPTS:

    enhanced = enhance_prompt(prompt)

    ow = len(prompt.split())
    ew = len(enhanced.split())

    original_words.append(ow)
    enhanced_words.append(ew)

    print("=" * 60)
    print("Original :", prompt)
    print("Enhanced :", enhanced)
    print("Original Words :", ow)
    print("Enhanced Words:", ew)
    print("=" * 60)


plt.figure(figsize=(10,6))

x = range(len(PROMPTS))
width = 0.35

bars1 = plt.bar(
    [i-width/2 for i in x],
    original_words,
    width,
    label="Original Prompt"
)

bars2 = plt.bar(
    [i+width/2 for i in x],
    enhanced_words,
    width,
    label="Enhanced Prompt"
)

plt.xticks(x, PROMPTS, rotation=15)
plt.ylabel("Word Count")
plt.xlabel("Prompt")
plt.title("Comparison of Original and Enhanced Prompts")
plt.legend()

# Add value labels
for bar in bars1:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height()+0.3,
        str(int(bar.get_height())),
        ha='center'
    )

for bar in bars2:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height()+0.3,
        str(int(bar.get_height())),
        ha='center'
    )

plt.grid(axis='y', linestyle='--', alpha=0.4)

os.makedirs("result_graphs", exist_ok=True)

plt.tight_layout()

plt.savefig(
    "result_graphs/prompt_enhancement_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGraph saved to result_graphs/prompt_enhancement_comparison.png")