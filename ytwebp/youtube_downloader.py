import ffmpeg 
from pytube import YouTube
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
