# phi_masking.py
import re

def deidentify_text(text: str) -> str:
    text = re.sub(r'\b(Dr|Mr|Ms|Mrs|Miss)\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?', '[NAME]', text)
    text = re.sub(r'\b[A-Z][a-z]+\s+[A-Z][a-z]+\b', '[FULL_NAME]', text)
    text = re.sub(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', '[DATE]', text)
    text = re.sub(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b',
                  '[MONTH]', text, flags=re.IGNORECASE)
    return text.strip()
