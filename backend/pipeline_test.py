from transformers import pipeline
import scipy

print("Loading MusicGen...")

pipe = pipeline(
    "text-to-audio",
    model="facebook/musicgen-small",
    device=-1
)

print("Generating music...")

music = pipe(
    "calm piano music for studying",
    forward_params={
        "max_new_tokens": 256
    }
)

print("Saving...")

scipy.io.wavfile.write(
    "outputs/musicgen_output.wav",
    rate=music["sampling_rate"],
    data=music["audio"]
)

print("Done!")