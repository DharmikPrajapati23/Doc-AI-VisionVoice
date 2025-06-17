import os
import base64
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def encode_image(image_path):
    """
    Encodes an image file to a base64 string.
    This is necessary for sending image data to API models that accept base64-encoded images.
    Returns None if image_path is None or empty.
    """
    if not image_path:
        return None
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

client = Groq()

VISION_MODEL = "meta-llama/llama-4-maverick-17b-128e-instruct"

def analyze_image_with_query(query, model, encoded_image=None):
    """
    Analyzes an image and/or responds to a text query using the specified Groq model.
    The image input is now optional.
    
    Args:
        query (str): The text query for the analysis.
        model (str): The name of the Groq model to use.
        encoded_image (str, optional): The base64-encoded image string. Defaults to None.
        
    Returns:
        str: The content of the model's response.
    """
    content_parts = [
        {
            "type": "text", 
            "text": query
        }
    ]

    if encoded_image: # Only add image if it's provided
        content_parts.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{encoded_image}",
                "detail": "high" 
            },
        })

    messages = [
        {
            "role": "user",
            "content": content_parts,
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model 
    )

    return chat_completion.choices[0].message.content
