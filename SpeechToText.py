import pyttsx3

engine = pyttsx3.init()

def textToMp3(text):
    engine.save_to_file(text, "speech.mp3")
    engine.runAndWait()