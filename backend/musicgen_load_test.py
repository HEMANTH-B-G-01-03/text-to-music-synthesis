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
from transformers import AutoProcessor
from transformers import MusicgenForConditionalGeneration
import time

print("Loading processor...")
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
print("Processor loaded")

print("Before model load")
start = time.time()

model = MusicgenForConditionalGeneration.from_pretrained(
    "facebook/musicgen-small",
    low_cpu_mem_usage=True
)

print("After model load")
print("Load time:", time.time() - start)

print("Moving to GPU...")
model = model.to("cuda")

print("GPU loaded successfully")