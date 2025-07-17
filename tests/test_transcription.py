#test_transcription.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.transcription.upload_save import run_transcription_pipeline

if __name__ == "__main__":
    audio_path = "C:\\Users\\dell\\Documents\\Python\\AI-medical-project\\data\\Patient_and_doctor_audio.mp4"  # Put your test file here
    sanitized_output = run_transcription_pipeline(audio_path)
    print("\n🧼 Sanitized Transcript:\n")
    print(sanitized_output)
