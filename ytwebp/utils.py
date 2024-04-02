from pytube import YouTube
import ffmpeg


def extract_video_url(url: str) -> str:
    yt = YouTube(url)
    streams = yt.streams.filter(file_extension='mp4', type="video")
    video_url = max(streams, key=lambda x: int(x.resolution[:-1])).url
    return video_url

def extract_video_info(url: str) -> dict:
    probe = ffmpeg.probe(url)
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    return video_info

def get_frame_rates(video_info: dict) -> int:
    return int(video_info["r_frame_rate"][:2])
