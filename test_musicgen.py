from transformers import AutoProcessor, MusicgenForConditionalGeneration
import torch

print("Step 1")

print("Loading processor...")
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
print("Processor loaded")

print("Loading model on CPU...")

model = MusicgenForConditionalGeneration.from_pretrained(
    "facebook/musicgen-small",
    torch_dtype=torch.float32,
    low_cpu_mem_usage=False
)

print("✅ Model loaded successfully!")