import os
import sys
import matplotlib.pyplot as plt

# Add project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

from backend.music_generator import generate_music

prompts = [
    "Happy flute music",
    "Calm piano melody",
    "Energetic rock music",
    "Relaxing guitar music",
    "Lo-fi study music"
]

file_sizes = []

print("\n========== Audio File Size Evaluation ==========\n")

for prompt in prompts:

    print(f"Generating: {prompt}")

    filepath = generate_music(prompt)

    # Size in MB
    size_mb = os.path.getsize(filepath) / (1024 * 1024)

    file_sizes.append(round(size_mb, 2))

    print(f"Saved: {filepath}")
    print(f"Size: {size_mb:.2f} MB\n")

# ---------------- Plot ---------------- #

plt.figure(figsize=(10,6))

bars = plt.bar(
    prompts,
    file_sizes
)

plt.title("Generated Audio File Size")
plt.xlabel("Input Prompt")
plt.ylabel("File Size (MB)")

plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+0.02,
        f"{bar.get_height():.2f}",
        ha="center",
        fontsize=10
    )

os.makedirs("result_graphs", exist_ok=True)

plt.tight_layout()

plt.savefig(
    "result_graphs/audio_file_size.png",
    dpi=300
)

plt.show()

print("\n✅ Graph saved successfully!")



