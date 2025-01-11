import cv2
import os

def play_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Set fullscreen mode
    cv2.namedWindow('Startup Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Startup Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        # Read the next frame from the video
        ret, frame = cap.read()
        if not ret:
            break
        # Display the frame
        cv2.imshow('Startup Video', frame)
        # Exit if the 'q' key is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the video file
    video_file = r"C:\Users\hp\Desktop\Video_startup\focus.mp4"
    if os.path.exists(video_file):
        play_video(video_file)
    else:
        print(f"Error: File '{video_file}' not found.")
