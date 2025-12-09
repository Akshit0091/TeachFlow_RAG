import whisper
import json

model = whisper.load_model("large-v2")

audio_path = r"D:\audio_test\About the Lectures.mp3"

result = model.transcribe(
    audio=audio_path,
    language="hi",
    task="translate",
    word_timestamps=False
)

print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

print(chunks)

with open("chunks_output.json", "w") as f:
    json.dump(chunks,f)
