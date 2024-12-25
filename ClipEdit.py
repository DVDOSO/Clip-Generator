from moviepy import *
import random
import mutagen
from mutagen.wave import WAVE
import math

def combineAudioWithVideo():
    speechLength = math.ceil(WAVE("speech.mp3").info.length)
    audioClip = AudioFileClip("speech.mp3")
    if(random.randint(0, 1)):
        videoClip = (
            VideoFileClip("Minecraft.mp4")
            .subclipped(0, speechLength)
            .with_volume_scaled(0.8)
        )
    else:
        videoClip = (
            VideoFileClip("SS.mp4")
            .subclipped(0, speechLength)
            .with_volume_scaled(0.8)
        )
    
    newAudioClip = CompositeAudioClip([audioClip])
    videoClip.audio = newAudioClip
    videoClip.write_videofile("result.mp4")


def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000


def create_subtitle_clips(subtitles, videosize):
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize
        
        text_clip = TextClip(
            font="BebasNeue-Regular.ttf",
            text=subtitle.text,
            font_size=35,
            color='white',
            stroke_color="black",
            stroke_width=5,
            size=(math.floor(video_width*7/8), None),
            method='caption',
            text_align='center'
        )

        subtitle_clips.append(text_clip.with_start(start_time).with_duration(duration).with_position('center'))

    return subtitle_clips
