# Simple Text-to-Speech (gTTS) Generator

A lightweight Python script that uses the Google Text-to-Speech (`gTTS`) library to convert a sample text string into an MP3 audio file.

---

## Features

* **Quick Conversion**: Instantly converts text strings into clear audio.
* **MP3 Output**: Automatically saves the generated audio locally as `voice.mp3`.
* **Error Handling**: Built-in `try-except` block to catch and report any unexpected issues gracefully.

---

## Prerequisites

Make sure you have **Python 3.x** installed on your system before proceeding.

---

## Installation

1. Clone or download this repository/script to your local machine.
2. Install the required `gTTS` library using `pip`:

   ```bash
   pip install gTTS
   ```
Usage

Run the script from your terminal or command prompt:

   ```Bash
      python your_script_name.py
   ```
Upon successful execution, you will see the following output in your console, and a voice.mp3 file will be created in your project directory:

```Audio saved successfully to voice.mp3```

Optional: Audio Playback on Linux

If you want the script to automatically play the audio file immediately after generation on a Linux system, ensure you have an audio player like mpg123 or mpv installed:
     
      ```Bash
      
      # Ubuntu / Debian
      sudo apt update && sudo apt install mpg123
      ```
Then, uncomment the following line in the Python script:
Python

      ```
      os.system("mpg123 voice.mp3")
      ```
