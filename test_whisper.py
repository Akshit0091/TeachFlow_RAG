import whisper
print("Package imported from:", whisper.__file__)

model = whisper.load_model("base")
print("Model loaded successfully!")
