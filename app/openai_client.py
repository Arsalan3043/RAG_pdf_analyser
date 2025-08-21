import os
import openai

# Use env variable or .env loader like python-dotenv if desired
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_comment(retrieved_chunks):
    """
    Uses OpenAI LLM to generate a comment sheet from retrieved document text.
    """
    prompt = (
        "Given the following material submittal excerpts:\n"
        + "\n".join(retrieved_chunks)
        + "\n\nPlease generate a comment sheet highlighting any missing data, unclear information, or potential compliance issues."
    )

    response = openai.Completion.create(
        engine="gpt-4",  # or "gpt-3.5-turbo-instruct"
        prompt=prompt,
        max_tokens=400,
        temperature=0.3,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()
