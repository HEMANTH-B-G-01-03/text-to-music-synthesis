# import torch
# from transformers import AutoProcessor, MusicgenForConditionalGeneration

# print("Loading processor...")

# processor = AutoProcessor.from_pretrained(
#     "facebook/musicgen-small"
# )

# print("Processor loaded")

# print("Loading model...")

# model = MusicgenForConditionalGeneration.from_pretrained(
#     "facebook/musicgen-small",
#     torch_dtype=torch.float16
# )

# print("Moving to GPU...")

# model = model.to("cuda")

# print("SUCCESS!")
import torch
import time

print("Step 1")

from transformers import AutoProcessor
print("Step 2")

from transformers import MusicgenForConditionalGeneration
print("Step 3")

print("Loading processor...")
processor = AutoProcessor.from_pretrained(
    "facebook/musicgen-small"
)
print("Processor loaded")

print("Loading config only...")
from transformers import AutoConfig

config = AutoConfig.from_pretrained(
    "facebook/musicgen-small"
)
print("Config loaded")

print("Starting model load...")

model = MusicgenForConditionalGeneration.from_pretrained(
    "facebook/musicgen-small",
    low_cpu_mem_usage=True
)

print("MODEL LOADED")