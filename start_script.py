import cv2
import pygame
import os
import screeninfo

def play_video(video_path, audio_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get the original video width and height
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Get screen information to center the video on the screen
    screen = screeninfo.get_monitors()[0]  # Get the primary monitor
    screen_width, screen_height = screen.width, screen.height

    # Set up pygame for audio playback
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Create a window with no resizing, based on the original video size
    cv2.namedWindow('Startup Video', cv2.WND_PROP_AUTOSIZE)  # Auto-size window based on video dimensions

    # Calculate the position to center the window
    x_pos = (screen_width - video_width) // 2
    y_pos = (screen_height - video_height) // 2

    # Move the window to the calculated position
    cv2.moveWindow('Startup Video', x_pos, y_pos)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Display the video at its original size
        cv2.imshow('Startup Video', frame)

        # Break the loop gracefully when 'q' is pressed or when the video ends
        if cv2.waitKey(25) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

if __name__ == "__main__":
    video_file = r"C:\Users\hp\Desktop\Video_startup\focus.mp4"  # Path to your video file
    audio_file = r"C:\Users\hp\Desktop\Video_startup\focus_audio.mp3"  # Path to your audio file

    if os.path.exists(video_file) and os.path.exists(audio_file):
        play_video(video_file, audio_file)
    else:
        print("Error: Video or Audio file not found.")
