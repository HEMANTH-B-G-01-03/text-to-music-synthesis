import os
import sys
import time
import matplotlib.pyplot as plt

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

# Import your project's music generation function
from backend.music_generator import generate_music

# Test prompts
prompts = [
    "Happy flute music",
    "Calm piano melody",
    "Energetic rock music",
    "Relaxing guitar music",
    "Lo-fi study music"
]

generation_times = []

print("\n========== Music Generation Time Evaluation ==========\n")

for prompt in prompts:

    print(f"Generating music for: {prompt}")

    start = time.perf_counter()

    # Call your actual project function
    generate_music(prompt)

    end = time.perf_counter()

    elapsed = round(end - start, 2)

    generation_times.append(elapsed)

    print(f"Completed in {elapsed} seconds\n")

# ---------------- Plot Graph ---------------- #

plt.figure(figsize=(10, 6))

bars = plt.bar(
    prompts,
    generation_times
)

plt.title("Music Generation Time for Different Prompts", fontsize=14)
plt.xlabel("Input Prompt", fontsize=12)
plt.ylabel("Generation Time (Seconds)", fontsize=12)

plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Add values on top of bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.2,
        f"{bar.get_height():.2f}s",
        ha="center",
        fontsize=10
    )

# Create output folder if not exists
os.makedirs("result_graphs", exist_ok=True)

plt.tight_layout()

plt.savefig(
    "result_graphs/music_generation_time.png",
    dpi=300
)

plt.show()

print("\n✅ Graph saved successfully!")
print("Location: result_graphs/music_generation_time.png")


