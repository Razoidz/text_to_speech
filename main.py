import os
import sys
import platform
from gtts import gTTS

# Get text from CLI arguments, or prompt if none were given
if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
else:
    text = input("Enter the text to convert to speech: ").strip()

if not text:
    print("No text provided. Exiting.")
    sys.exit(1)

try:
    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")
    print("Audio saved successfully to voice.mp3")
    
    # Optional: If you want to play it immediately on Linux, 
    # ensure 'mpg123' or 'mpv' is installed on your host Linux system.
    # os.system("mpg123 voice.mp3")

except Exception as e:
    print(f"An error occurred: {e}")



def play_audio(filename="voice.mp3"):
    system = platform.system()
    print(f"Playing {filename}...")
    
    try:
        if system == "Linux":
            # Tries mpg123 first, falls back to mpv or ffplay if available
            os.system(f"mpg123 {filename} 2>/dev/null || mpv {filename} 2>/dev/null || ffplay -nodisp -autoexit {filename} 2>/dev/null")
        elif system == "Darwin":  # macOS
            os.system(f"afplay {filename}")
        elif system == "Windows":
            os.system(f"start {filename}")
        else:
            print(f"Unsupported operating system: {system}")
    except Exception as e:
        print(f"An error occurred while playing audio: {e}")

if __name__ == "__main__":
    play_audio()