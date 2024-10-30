import requests
import logging
import config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def text_to_speech(text, filename="eidos_thought.mp3", voice_id="YOUR_ELEVENLABS_VOICE_ID"):
    """
    Converts text to speech using ElevenLabs API and saves the output as an MP3 file.
    Args:
        text (str): The text to convert to audio.
        filename (str): The filename to save the audio file.
        voice_id (str): The ElevenLabs voice ID to use for synthesis.
    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": config.ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.9
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        with open(filename, "wb") as audio_file:
            audio_file.write(response.content)
        logging.info(f"Audio file saved as {filename}")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to synthesize text to speech: {e}")
        return False

if __name__ == "__main__":
    sample_text = "This is a sample thought from Eidos, contemplating the nature of technology."
    success = text_to_speech(sample_text)
    if success:
        print(f"Audio successfully saved to 'eidos_thought.mp3'")
    else:
        print("Audio generation failed.")
