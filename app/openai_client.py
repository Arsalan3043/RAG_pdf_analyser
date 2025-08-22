import os
import openai
from dotenv import load_dotenv
load_dotenv()

# Use env variable or .env loader like python-dotenv if desired
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_comment(retrieved_chunks):
    """
    Uses OpenAI ChatCompletion to generate a comment sheet from retrieved document text.
    """
    prompt = (
        "Given the following material submittal excerpts:\n"
        + "\n".join(retrieved_chunks)
        + "\n\nPlease generate a comment sheet highlighting any missing data, unclear information, or potential compliance issues."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or use "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are an expert QA/QC engineer for construction material submittals."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.3,
        n=1
    )
    return response['choices'][0]['message']['content'].strip()
