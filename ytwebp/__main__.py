import frame_extractor
import animator
import youtube_downloader
import sys

if __name__ == "__main__":
    try:
        test_url = sys.argv[1]
    except:
        test_url = "https://youtu.be/lymwKICWEsA?si=NOhswUENAVFS_mVB"
    output = "output"
    video_url = "temp.mp4"
    youtube_downloader.download_video(test_url, "00:00:00", 2, "temp")
    duration = frame_extractor.get_video_duration_seconds(video_url) 
    frames = frame_extractor.extract_frames(video_url)
    animator.animate_images_array(frames, duration, output)
