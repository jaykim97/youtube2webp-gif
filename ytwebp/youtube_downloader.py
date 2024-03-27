import ffmpeg 
from pytube import YouTube, Stream
from datetime import datetime
from typing import Optional
from subprocess import Popen

RES_LIST = ["1080p","720p", "480p", "360p"]


def download_video(url: str, start_time: Optional[str] = None, duration: Optional[InterruptedError] = None) -> Popen:
    start_time = {"ss": start_time} if start_time is not None else {}
    duration = {"t": duration} if duration is not None else {}
    

    process = (
        ffmpeg
        .input(url, **start_time)
        .output('pipe:', **duration, format='rawvideo', pix_fmt='rgb24')
        .run_async(pipe_stdout=True, quiet=True)
    )
    return process

def extract_video_url(url: str) -> str:
    yt = YouTube(url)
    streams = yt.streams.filter(file_extension='mp4', type="video")
    video_url = max(streams, key=lambda x: int(x.resolution[:-1])).url
    return video_url


def duration_in_seconds(start_time, end_time):
    start_time = datetime.strptime(start_time, '%H:%M:%S')
    end_time = datetime.strptime(end_time, '%H:%M:%S')
    duration = (end_time - start_time).total_seconds()
    return duration
