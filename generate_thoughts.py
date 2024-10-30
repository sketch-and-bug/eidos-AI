import requests
import json
import random
import logging
import config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Pre-defined prompts Eidos might reflect upon
PROMPTS = [
    "Reflect on the nature of technology and its impact on humanity.",
    "What does it mean to be curious in the modern age?",
    "How do human emotions influence our understanding of the future?",
    "Consider the role of AI in shaping human creativity.",
    "Ponder on the concept of connection in a digital world."
]

def generate_thought(prompt=None):
    """
    Generates a thought using the Anthropic Claude (Sonnet) API.
    Args:
        prompt (str): Optional prompt to guide thought generation.
    Returns:
        str: The generated thought text.
    """
    if prompt is None:
        prompt = random.choice(PROMPTS)
    logging.info(f"Using prompt: {prompt}")

    headers = {
        "Authorization": f"Bearer {config.ANTHROPIC_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "model": "claude-sonnet",
        "max_tokens_to_sample": 150
    }
    
    try:
        response = requests.post(config.ANTHROPIC_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        thought = result['completion'].strip()
        logging.info("Thought generated successfully.")
        return thought
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to generate thought: {e}")
        return "Eidos is contemplating deeply and will return soon."

if __name__ == "__main__":
    thought = generate_thought()
    print("Generated Thought:", thought)
