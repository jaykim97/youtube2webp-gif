import frame_extractor
import animator
import youtube_downloader
import sys
import utils
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Turn section of youtube video into animated webp")
    parser.add_argument('url', type=str, help='URL of the YouTube video to process')
    parser.add_argument('-s', '--start-time', type=str, help='Start time for the video (format: HH:MM:SS)')
    parser.add_argument('-d', '--duration', type=int, help='Duration of the video to process (in seconds)')
    args = parser.parse_args()
    
    url = utils.extract_video_url(args.url)
    print("video url extracted")
    process = youtube_downloader.download_video(url, start_time = args.start_time, duration = args.duration)
    print("video extraction complete")
    video_info = utils.extract_video_info(url)
    print("video info extration complete")
    frames = frame_extractor.extract_frames(process,video_info)
    fps = utils.get_frame_rates(video_info)
    print("frame extraction complete")
    animator.animate_images_array(frames, fps, "output1")