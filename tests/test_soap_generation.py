
# test_soap_generation.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.soap_generation.gemini_soap import generate_soap_note
from services.soap_generation.gemini_soap import generate_soap_note

if __name__ == "__main__":
    # Sample input (normally output from your transcript + PHI masking)
    sample_transcript = (
        "Patient reports chest pain for the last two days, especially when climbing stairs. "
        "Doctor asks about medical history, listens to heart and lungs, orders ECG."
    )

    soap_note = generate_soap_note(sample_transcript)
    print("\n📝 Generated SOAP Note:\n")
    print(soap_note)
