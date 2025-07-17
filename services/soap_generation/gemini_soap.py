# gemini_soap.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_soap_note(sanitized_text: str) -> str:
    print("🧠 Generating SOAP note using Gemini...")
    
    prompt = f"""
    You are a medical scribe. Convert the following doctor-patient conversation into a structured SOAP note:

    Format:
    **Subjective**: ...
    **Objective**: ...
    **Assessment**: ...
    **Plan**: ...

    Transcript:
    {sanitized_text}
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    soap_note = response.text.strip()

    # Optional: Save to file
    with open("soap_note.txt", "w", encoding="utf-8") as f:
        f.write(soap_note)

    return soap_note
