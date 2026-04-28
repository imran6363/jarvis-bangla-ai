from gtts import gTTS
import os
from playsound import playsound

def speak(text):
    try:
        tts = gTTS(text=text, lang='bn')
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except:
        print("Voice error")
