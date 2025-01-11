from moviepy.editor import VideoFileClip

def play_video_with_audio(video_path):
    try:
        # Load and play the video with audio
        clip = VideoFileClip(video_path)
        clip.preview()  # Plays the video and audio
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Path to the video file
    video_file = r"C:\Users\hp\Desktop\Video_startup\focus.mp4"
    if os.path.exists(video_file):
        play_video_with_audio(video_file)
    else:
        print(f"Error: File '{video_file}' not found.")
