import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

def generate_image(prompt: str, resolution: int = 512) -> str:
    """
    Call OpenAI's image API (or any other service) to generate an image.
    Returns the URL of the generated image.
    """
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not found in environment")

    # Force resolution to allowed sizes
    if resolution not in [256, 512, 1024]:
        raise ValueError(f"Resolution {resolution}x{resolution} not supported")

    size_str = f"{resolution}x{resolution}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    payload = {
        "prompt": prompt,
        "n": 1,
        "size": size_str
    }

    resp = requests.post("https://api.openai.com/v1/images/generations", json=payload, headers=headers)
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to generate image: {resp.text}")

    data = resp.json()
    return data["data"][0]["url"]
