import pyttsx3
from moviepy import *
import math
import mutagen
from mutagen.wave import WAVE

engine = pyttsx3.init()

def textToMp3Short(text):
    engine.save_to_file(text, "speech.mp3")
    engine.runAndWait()

    speechLength = WAVE("speech.mp3").info.length
    audioClip = AudioFileClip("speech.mp3")

    currentTime = 0
    id = 0
    while(currentTime <= speechLength):
        if(currentTime + 60 <= speechLength):
            #CompositeAudioClip([audioClip]).subclipped(currentTime, currentTime + 30)
            newAudioClip = audioClip.subclipped(currentTime, currentTime + 30)
            newAudioClip.write_audiofile(f"./output/speech{id}.mp3")
            currentTime += 29
            id += 1
        else:
            newAudioClip = audioClip.subclipped(currentTime, speechLength)
            newAudioClip.write_audiofile(f"./output/speech{id}.mp3")
            currentTime += 999