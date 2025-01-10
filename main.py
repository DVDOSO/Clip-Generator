import SpeechToText, ClipEdit, Subtitles, pysrt, os, datetime
from moviepy import *

def deleteFile(delFile):
    if os.path.exists(delFile):
        os.remove(delFile)
    else:
        print("Error")

def generate(text):
    SpeechToText.textToMp3Short(text)

    i = 0
    for speech in os.listdir('./output'):
        Subtitles.genSubtitlesShort(f'./output/{speech}', i)
        i += 1
    
    i = 0
    for item in os.listdir('./output'):
        if(item[:6] == 'speech'):
            ClipEdit.createVideoShorts(f'./output/{item}', f'./output/output{item[6:-4]}.srt', i)
            i += 1

    for item in os.listdir('./output'):
        if(item[:6] == 'speech'):
            deleteFile(f'./output/{item}')
        if(item[:6] == 'output'):
            deleteFile(f'./output/{item}')
    deleteFile('speech.mp3')

text = ""
print("Paste your text here. Type # on a new line to end the input:\n")
while True:
    line = input()
    if(line == '#'): break
    else:
        text = text + line

generate(text)