import ffmpeg 
from pytube import YouTube, Stream
from datetime import datetime

RES_LIST = ["1080p","720p", "480p", "360p"]


def download_video(url, start_time, duration, output_file):
    url = _extract_video_url(url)
    out, _ = (
        ffmpeg
        .input(url, ss=start_time)
        .output(f"{output_file}.mp4", t=duration, format='mp4', vcodec='copy', acodec='copy')
        .run()
    )
    return f"{output_file}.mp4"

def _extract_video_url(url: str) -> str:
    yt = YouTube(url)
    streams = yt.streams.filter(file_extension='mp4', type="video")
    video_url = max(streams, key=lambda x: int(x.resolution[:-1])).url
    return video_url


def duration_in_seconds(start_time, end_time):
    start_time = datetime.strptime(start_time, '%H:%M:%S')
    end_time = datetime.strptime(end_time, '%H:%M:%S')
    duration = (end_time - start_time).total_seconds()
    return duration
