import SpeechToText, ClipEdit, Subtitles, pysrt, os, datetime
from moviepy import *

def deleteFile(delFile):
    if os.path.exists(delFile):
        os.remove(delFile)
    else:
        print("Error")

def timeToString():
    date = datetime.datetime
    year = date.now().year
    month = date.now().month
    day = date.now().day
    hour = date.now().hour
    minute = date.now().minute
    second = date.now().second
    return f"{year}{month}{day}{hour}{minute}{second}"

def generate(text):
    SpeechToText.textToMp3(text)
    ClipEdit.combineAudioWithVideo()
    Subtitles.genSubtitles()

    video = VideoFileClip('result.mp4')
    subtitles = pysrt.open('output.srt')

    subtitle_clips = ClipEdit.create_subtitle_clips(subtitles, video.size)
    final_video = CompositeVideoClip([video] + subtitle_clips)
    final_video.write_videofile('final.mp4')
    
    os.rename("final.mp4", "./output/"+timeToString()+".mp4")

    deleteFile("result.mp4")
    deleteFile("speech.mp3")
    deleteFile("output.srt")

generate("""
A couple of weeks ago, I traveled to another country to see an artist I’ve been a fan of for six years. This was a once-in-a-lifetime experience for me, and I’d been waiting months for it. I sacrificed a lot financially and mentally to make it happen. Since it was my first (and probably only) time seeing them, I went all out: I bought GA tickets and arrived at the queue at 5 a.m. (even though the doors wouldn’t open until 6:30–7 p.m.) in freezing cold weather. I waited all day—hungry, cold, and dehydrated—but it was worth it because when the doors opened, I secured a front-row barricade spot, right up against the stage. This was my dream spot.

Then, a guy behind me tapped me on the shoulder and told me he was disabled. He said the venue was supposed to let disabled attendees in early, but they hadn’t. He asked me to give him my spot at the barricade. Here’s the thing: I know this venue is very accommodating for disabled attendees. I actually have friends with disabilities who’ve gone to shows here, and the staff always ensures they get to the front row safely during a designated time frame before it gets too crowded. 

Now, I’m a very short person (155 cm/5’1”), and this guy was extremely tall—easily over 5.5 If I gave him my spot, I wouldn’t be able to see anything at all because he would completely block my view. I honestly would’ve been willing to move if he wasn’t so tall or if I could still see from the second row. However, in this case, I knew I’d lose the view I had waited more than 10 hours for.

I tried to compromise. I pointed out that the right side of the barricade was still open and suggested he go there. Since he’s so tall, he’d still have a great view and could hold onto the rail for support. However, he refused, saying the view wasn’t as good as where I was. While we were talking, that section filled up, and he became more insistent. He said he’d "have a hard time" if he couldn’t take my spot.
""")