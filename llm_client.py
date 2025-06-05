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
MAX_CHARS_FOR_LLM = 10000  # Adjust based on model and needs

def summarize_text(text: str) -> str:
    
    if not text or not text.strip():
        return "No data provided to summarize."

    # Check for error text from previous steps
    if text.startswith("Error:"):
        return f"Skipping summarization due to previous error: {text}"

    # Truncate very long texts to avoid hitting token limits
    if len(text) > MAX_CHARS_FOR_LLM:
        text = text[:MAX_CHARS_FOR_LLM] + "\n... [CONTENT TRUNCATED FOR LLM INPUT]"
        print(f"Warning: Input text was truncated to {MAX_CHARS_FOR_LLM} characters for LLM.")

    try:
        model = genai.GenerativeModel(MODEL)
        
        # Create a more structured prompt that explicitly includes the data
        prompt = f"""Analyze and summarize the following gene data. The data is in Metta format, containing gene information including identifiers, types, chromosomal locations, and properties.

GENE DATA:
{text}

Format the response in clear, bullet-point style."""

        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.4,
                max_output_tokens=1024,
            )
        )

        if response.text:
            summary = response.text.strip()
            print("Gemini summary generated successfully.")
            return summary
        else:
            print("Warning: Empty response received from Gemini API")
            return "Error: Received empty response from Gemini API."

    except Exception as e:
        error_msg = f"Error calling Gemini API: {str(e)}"
        print(error_msg)
        return f"Error generating summary: {str(e)}" 