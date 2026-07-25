import os
import matplotlib.pyplot as plt

OUTPUT_FOLDER = "outputs"

files = []
sizes = []

for file in os.listdir(OUTPUT_FOLDER):

    if file.endswith(".wav"):

        path = os.path.join(OUTPUT_FOLDER, file)

        size = os.path.getsize(path)/(1024*1024)

        files.append(file[:8])
        sizes.append(round(size,2))

plt.figure(figsize=(10,6))

plt.bar(files, sizes)

plt.xlabel("Generated Audio Files")
plt.ylabel("File Size (MB)")
plt.title("Generated Audio File Sizes")

plt.tight_layout()

os.makedirs("result_graphs", exist_ok=True)

plt.savefig(
    "result_graphs/output_audio_file_size.png",
    dpi=300
)

plt.show()

print("\nGraph saved successfully!")