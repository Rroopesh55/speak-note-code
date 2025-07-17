# whisper_transcribe.py
import whisper

def transcribe_audio(file_path: str) -> str:
    print("🔊 Loading Whisper model...")
    model = whisper.load_model("base")
    print(f"🎙️ Transcribing: {file_path}")
    result = model.transcribe(file_path)
    return result["text"]
