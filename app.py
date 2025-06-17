from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr
from groq import Groq 
import uuid

from brain_of_the_doctor import encode_image, analyze_image_with_query, VISION_MODEL 
from voice_of_the_doctor import text_to_speech_with_elevenlabs

groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

system_prompt = """You are acting as a professional doctor for learning purposes.
ONly give Medical related answer.
if user ask other filed question except Medicala field simple response sorry i can't help i am specialised in medical Field 
Provide a clear and concise response based on the input. If an image is provided, analyze it. 
If only text is provided, respond to the question directly. 
If you offer a potential diagnosis or advice, please suggest some general remedies or next steps. 
Do not use any numbers or special characters in your response. Your answer should be concise, ideally no more than two sentences. 
Please start your answer immediately without any preamble, as if you are speaking directly to a patient."""


def process_inputs(text_question, image_filepath):
    """
    Processes text and optionally image inputs to generate a doctor's response and corresponding audio.
    
    Args:
        text_question (str): The text question typed by the user.
        image_filepath (str): Path to the uploaded image file (can be None).
        
    Returns:
        tuple: (user_question_text, doctor_response_text, doctor_response_audio_path)
    """
    user_question_text = text_question 
    doctor_response = ""
    encoded_image = None

    if image_filepath:
        encoded_image = encode_image(image_filepath)
        if encoded_image is None: # Handle cases where image encoding failed
            doctor_response = "There was an issue processing the image. Please try again or ask a text-only question."
            final_audio_path = text_to_speech_with_elevenlabs(
                input_text=doctor_response, 
                output_filepath=f"error_response_{uuid.uuid4()}.mp3" # Unique filename for error audio
            )
            return user_question_text, doctor_response, final_audio_path

    full_query = system_prompt + " " + user_question_text 
    
    doctor_response = analyze_image_with_query(
        query=full_query, 
        encoded_image=encoded_image, # Pass None if no image, or the encoded image
        model=VISION_MODEL 
    )


    unique_id = uuid.uuid4()
    doctor_response_audio_filepath = f"doctor_response_{unique_id}.mp3"
    
    final_audio_path = text_to_speech_with_elevenlabs(
        input_text=doctor_response, 
        output_filepath=doctor_response_audio_filepath
    ) 


    return user_question_text, doctor_response, final_audio_path



iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Textbox(label="Type your question here", placeholder="e.g., I have a headache what should I do? Or, Is there something wrong with my face?"),
        gr.Image(type="filepath", label="Upload an Image (Optional)", interactive=True)
    ],
    outputs=[
        gr.Textbox(label="Your Question"),
        gr.Textbox(label="Doctor's Response (Text)"),
        gr.Audio(label="Doctor's Response (Audio)", autoplay=True) 
    ],
    title="AI Doctor with Vision and Voice",
    description="Ask a question by typing and optionally upload an image for analysis to get a medical response from the AI Doctor."
)

# Launch the Gradio app
iface.launch(debug=True, share=True)
