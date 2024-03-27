import frame_extractor
import animator
import youtube_downloader
import sys

if __name__ == "__main__":
    try:
        test_url = sys.argv[1]
    except:
        test_url = "https://youtu.be/lymwKICWEsA?si=NOhswUENAVFS_mVB"
    
    
    test_url = youtube_downloader.extract_video_url(test_url)
    process = youtube_downloader.download_video(test_url, duration=2)
    frames = frame_extractor.extract_frames(test_url, process)
    animator.animate_images_array(frames, 2, "output")