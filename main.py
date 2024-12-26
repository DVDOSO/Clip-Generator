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

generate("""
This one is general. I am a guy who, when I don't enjoy something, I'll tell you I don't, but if I commit to something, I'll see it through to the end without complaining.

This comes to a head where I was on vacation with my older brother in Arizona, who wanted to do a lot of nature hikes. Nature hikes are fine. I don't mind them, but I do dislike walking up large hills. Walking downhill is the easiest thing ever, it's like being nature's passenger princess. You just put your foot forward and let gravity do all the work. Walking uphill conversely is very draining and leaves me sweaty.

I don't make a point to complain about something when I do it, so when I was walking uphill, despite not liking it much, I held basic conversation with my brother.

As we were heading back down, he asked me if I was having fun and I said no. Not because of any fault of my brother, I just didn't find the activity fun. Not even bad, just satisfactory. Later when he was driving me to the airport for my flight home he told me "If I ask you if you're having fun, don't say 'no.'"

I understand that it can be demoralizing to hear someone's not having fun, but I don't like it when people ask for my opinion and get upset when I give my honest answer. If I'm not having fun, I'll just say I'm not having fun.
""")