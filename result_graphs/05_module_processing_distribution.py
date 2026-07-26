import os
import matplotlib.pyplot as plt

modules = [
    "Prompt\nEnhancement",
    "Music\nGeneration",
    "Recommendation",
    "Audio\nSaving"
]

# Distribution percentages (illustrative)
distribution = [
    5,
    82,
    8,
    5
]

plt.figure(figsize=(8, 8))

plt.pie(
    distribution,          # <-- Changed from 'times' to 'distribution'
    labels=modules,
    autopct="%1.1f%%",
    startangle=90,
    explode=(0.03, 0.06, 0.03, 0.03),  # Slightly highlight slices
    shadow=True
)

plt.title(
    "Module Processing Time Distribution",
    fontsize=15,
    fontweight="bold"
)

plt.axis("equal")

os.makedirs("result_graphs", exist_ok=True)

plt.tight_layout()

plt.savefig(
    "result_graphs/module_processing_distribution.png",
    dpi=300
)

plt.show()

print("✅ Graph saved successfully!")