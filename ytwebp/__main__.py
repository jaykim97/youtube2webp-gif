import frame_extractor
import animator
if __name__ == "__main__":
    video_url = "example.mp4"
    output = "output"
    duration = frame_extractor.get_video_duration_seconds(video_url) 
    frames = frame_extractor.extract_frames(video_url)
    animator.animate_images_array(frames, duration, output)
