from transformers import MusicgenForConditionalGeneration, AutoProcessor
import soundfile as sf
import torch
import numpy as np

def generate_music(prompt: str, duration: int = 8, output_path: str = "outputs/output.wav"):
    print(f"Loading model...")
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    print(f"Running on: {device}")

    inputs = processor(text=[prompt], padding=True, return_tensors="pt").to(device)

    tokens = duration * model.config.audio_encoder.frame_rate
    wav = model.generate(**inputs, max_new_tokens=int(tokens))

    audio = wav[0, 0].cpu().numpy()
    sf.write(output_path, audio, samplerate=32000)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    generate_music("calm piano melody for studying", duration=8)