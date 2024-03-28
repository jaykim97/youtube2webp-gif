import frame_extractor
import animator
import youtube_downloader
import sys
import utils

if __name__ == "__main__":
    try:
        test_url = sys.argv[1]
    except:
        test_url = "https://youtu.be/lymwKICWEsA?si=NOhswUENAVFS_mVB"
    
    
    test_url = utils.extract_video_url(test_url)
    print("video url extracted")
    process = youtube_downloader.download_video(test_url, duration=4)
    print("video extraction complete")
    video_info = utils.extract_video_info(test_url)
    print("video info extration complete")
    frames = frame_extractor.extract_frames(process,video_info)
    print("frame extraction complete")
    animator.animate_images_array(frames, "output2")