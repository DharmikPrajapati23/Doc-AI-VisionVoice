import os
import elevenlabs
from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv
load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    """
    Converts text to speech using ElevenLabs API and saves the audio.
    Server-side playback (e.g., with playsound) has been removed,
    as Gradio's gr.Audio component will handle playing the audio in the browser.
    
    Args:
        input_text (str): The text to convert to speech.
        output_filepath (str): The path where the audio file will be saved.
        
    Returns:
        str: The path to the saved audio file.
    """
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="OYTbf65OHHFELVut7v2H",
        output_format="mp3_22050_32", # Keep as MP3
        model_id="eleven_turbo_v2"
    )


    try:
        elevenlabs.save(audio, output_filepath)
        print(f"Audio saved to: {output_filepath}")
    except Exception as e:
        print(f"Error saving audio file {output_filepath}: {e}")
        return None 
    
    return output_filepath 
