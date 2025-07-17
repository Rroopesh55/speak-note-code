# upload_save.py
from .whisper_transcribe import transcribe_audio
from .phi_masking import deidentify_text

def run_transcription_pipeline(audio_path: str) -> str:
    raw = transcribe_audio(audio_path)
    sanitized = deidentify_text(raw)

    # Optional: save for debugging
    with open("transcript_sanitized.txt", "w", encoding="utf-8") as f:
        f.write(sanitized)

    return sanitized
