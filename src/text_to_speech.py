import pyttsx3
import os

# Initialize the engine
audio_engine = pyttsx3.init()
rate = audio_engine.getProperty("rate")
audio_engine.setProperty("rate", rate + 35)

# Set save directory by changing the current working directory to audiofiles folder

def Text_To_Speech(texts, file_directory):
      save_directory = file_directory
      os.chdir(save_directory)

      audio_engine.save_to_file(texts[0], "TITLE.mp3")
      audio_engine.runAndWait()
      audio_engine.save_to_file(texts[1], "CONTENT.mp3")
      audio_engine.runAndWait()