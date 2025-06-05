import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    exit(1)

try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Error configuring Gemini API: {str(e)}")
    exit(1)

MODEL = 'gemini-1.5-flash-latest'


def summarize_text(text: str) -> str:
    """
    Send the input text to the Gemini LLM and return the summary.
    """
    if not text.strip():
        return "No data to summarize."
    
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(
            f"Summarize the following gene data in a human-readable way:\n{text}",
            generation_config=genai.types.GenerationConfig(
                temperature=0.5,
                max_output_tokens=512,
            )
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {str(e)}")
        return "Error generating summary." 