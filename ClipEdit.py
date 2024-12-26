from moviepy import *
import random
import math
import pysrt
import datetime

# def combineAudioWithVideo(audio):
#     speechLength = math.ceil(WAVE(audio).info.length)
#     audioClip = AudioFileClip(audio)
#     if(random.randint(0, 1)):
#         videoClip = (
#             VideoFileClip("Minecraft.mp4")
#             .subclipped(0, speechLength)
#             .with_volume_scaled(0.8)
#         )
#     else:
#         videoClip = (
#             VideoFileClip("SS.mp4")
#             .subclipped(0, speechLength)
#             .with_volume_scaled(0.8)
#         )
    
#     newAudioClip = CompositeAudioClip([audioClip])
#     videoClip.audio = newAudioClip
#     videoClip.write_videofile(f"clip{id}.mp4")

def timeToString():
    date = datetime.datetime
    year = date.now().year
    month = date.now().month
    day = date.now().day
    hour = date.now().hour
    minute = date.now().minute
    second = date.now().second
    return f"{year:02d}{month:02d}{day:02d}{hour:02d}{minute:02d}{second:02d}"

def createVideoShorts(speech, subtitles, id):
    audioClip = AudioFileClip(speech)
    speechLength = audioClip.duration
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
    
    subtitle_clips = create_subtitle_clips(pysrt.open(subtitles), videoClip.size)

    music = AudioFileClip("music.mp3").with_volume_scaled(0.1)
    sfx = AudioFileClip("sfx.mp3").with_volume_scaled(0.3).with_duration(4)

    newAudioClip = CompositeAudioClip([audioClip, music, sfx]).subclipped(0, speechLength)
    videoClip.audio = newAudioClip
    finalVideo = CompositeVideoClip([videoClip] + subtitle_clips)
    finalVideo.write_videofile(f"./output/{timeToString()}clip{id}.mp4")


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
            font_size=45,
            color='white',
            stroke_color="black",
            stroke_width=5,
            size=(math.floor(video_width*7/8), None),
            method='caption',
            text_align='center'
        )

        subtitle_clips.append(text_clip.with_start(start_time).with_duration(duration).with_position('center'))

    return subtitle_clips
