import whisper
import stable_whisper
import datetime

def srt_timestamp(seconds: float) -> str:
    """Convert a float timestamp (in seconds) to SRT time format (HH:MM:SS,mmm)."""
    td = datetime.timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = td.microseconds // 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

model = stable_whisper.load_model("tiny.en")

def genSubtitlesShort(media, id):
    result = model.transcribe(media, fp16=False)

    result.to_srt_vtt(f'./output/output{id}.srt', segment_level=False)

    # segments = result["segments"]

    # with open(f"./output/output{id}.srt", "w", encoding="utf-8") as srt_file:
    #     for i, segment in enumerate(segments, start=1):
    #         start_time = srt_timestamp(segment["start"])
    #         end_time = srt_timestamp(segment["end"])
    #         text = segment["text"].strip()

    #         srt_file.write(f"{i}\n")
    #         srt_file.write(f"{start_time} --> {end_time}\n")
    #         srt_file.write(f"{text}\n\n")