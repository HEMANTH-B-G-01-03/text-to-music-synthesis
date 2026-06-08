# from transformers import MusicgenForConditionalGeneration, AutoProcessor
# import soundfile as sf
# import torch
# import numpy as np

# def generate_music(prompt: str, duration: int = 8, output_path: str = "outputs/output.wav"):
#     print(f"Loading model...")
#     processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
#     model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

#     device = "cuda" if torch.cuda.is_available() else "cpu"
#     model = model.to(device)
#     print(f"Running on: {device}")

#     inputs = processor(text=[prompt], padding=True, return_tensors="pt").to(device)

#     tokens = duration * model.config.audio_encoder.frame_rate
#     wav = model.generate(**inputs, max_new_tokens=int(tokens))

#     audio = wav[0, 0].cpu().numpy()
#     sf.write(output_path, audio, samplerate=32000)
#     print(f"Saved to {output_path}")

# if __name__ == "__main__":
#     generate_music("calm piano melody for studying", duration=8)




import torch
import soundfile as sf
import numpy as np

print("PyTorch:", torch.__version__)
print("CUDA:", torch.cuda.is_available())

from transformers import AutoProcessor, MusicgenForConditionalGeneration

print("Loading processor...")
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
print("Processor loaded!")

print("Loading model...")
model = MusicgenForConditionalGeneration.from_pretrained(
    "facebook/musicgen-small",
    torch_dtype=torch.float16
)
print("Model loaded!")

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)
print(f"Model moved to: {device}")

prompt = "calm piano melody for studying"
inputs = processor(text=[prompt], padding=True, return_tensors="pt").to(device)
print("Generating music...")

with torch.no_grad():
    wav = model.generate(**inputs, max_new_tokens=256)

print("Generation done!")
audio = wav[0, 0].cpu().numpy().astype(np.float32)
sf.write("outputs/output.wav", audio, samplerate=32000)
print("Saved to outputs/output.wav")