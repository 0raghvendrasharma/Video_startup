import cv2
import os
import pygame

def play_video_with_audio(video_path):
    # Initialize pygame mixer for audio
    pygame.init()
    pygame.mixer.init()

    # Load the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Extract the audio track and play it
    try:
        pygame.mixer.music.load(video_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error: Could not play audio. {e}")
        return

    # Create a window with the video resolution
    cv2.namedWindow('Startup Video', cv2.WINDOW_NORMAL)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:  # If the video ends
            break

        # Display the video frame
        cv2.imshow('Startup Video', frame)

        # Exit on pressing 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Stop audio playback and release resources
    pygame.mixer.music.stop()
    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == "__main__":
    # Path to the video file
    video_file = r"C:\Users\hp\Desktop\Video_startup\focus.mp4"
    if os.path.exists(video_file):
        play_video_with_audio(video_file)
    else:
        print(f"Error: File '{video_file}' not found.")
