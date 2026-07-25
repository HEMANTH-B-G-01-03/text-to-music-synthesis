import os
import time
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

processing_times = []

print("\n========== Prompt Processing Time Evaluation ==========\n")

for prompt in prompts:

    print(f"Processing: {prompt}")

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": "Enhance the given music prompt by adding musical style, mood, instruments, tempo and atmosphere."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 120
    }

    start = time.perf_counter()

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload
    )

    end = time.perf_counter()

    elapsed = round(end - start, 2)

    processing_times.append(elapsed)

    print(f"Completed in {elapsed} seconds")

# ---------------- Plot ---------------- #

plt.figure(figsize=(10,6))

bars = plt.bar(
    prompts,
    processing_times
)

plt.title("Prompt Processing Time using Qwen2.5")
plt.xlabel("Input Prompt")
plt.ylabel("Processing Time (Seconds)")

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.xticks(rotation=15)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+0.03,
        f"{bar.get_height():.2f}s",
        ha="center",
        fontsize=10
    )

os.makedirs("result_graphs", exist_ok=True)

plt.tight_layout()

plt.savefig(
    "result_graphs/prompt_processing_time.png",
    dpi=300
)

plt.show()

print("\n✅ Graph saved successfully!")