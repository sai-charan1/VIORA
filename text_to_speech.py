import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
from dotenv import load_dotenv
from playsound import playsound
from gtts import gTTS

load_dotenv()
ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id="ZF6FPAbjXT4488VcRRnw", #"JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format= "mp3_22050_32",
    )
    elevenlabs.save(audio, output_filepath)
    
    try:
        playsound(output_filepath)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")



def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    try:
        playsound(output_filepath)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


## input_text = "Hi, I am doing fine, how are you? This is a testing?"
## output_filepath = "test_text_to_speech.mp3"
## text_to_speech_with_elevenlabs(input_text, output_filepath)
