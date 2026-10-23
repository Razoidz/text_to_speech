import os
from gtts import gTTS

text = "Settings for the bot test"

try:
    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")
    print("Audio saved successfully to voice.mp3")
    
    # Optional: If you want to play it immediately on Linux, 
    # ensure 'mpg123' or 'mpv' is installed on your host Linux system.
    # os.system("mpg123 voice.mp3")

except Exception as e:
    print(f"An error occurred: {e}")
