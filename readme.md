# 🎯 Focused Startup Video - Stay Motivated and Productive 

## 🚀 Motivation

This project was born from my own struggle with distractions. I often found myself losing focus when starting my laptop. Inspired by a motivational video of Krishna advising Arjun to focus, I created this app to help myself (and others like me) stay focused the moment we open our laptops. Now, a **motivational video** plays at startup, reminding you to stay on task and avoid distractions. 🧘‍♂️

---

## ✨ Features

- **🎥 Motivational Video & Audio**: Plays an inspiring video with audio to kickstart your day.
- **🖥️ Auto-Play on Startup**: The video automatically plays when you log in, setting the tone for your day.
- **🔒 Workstation Unlock**: Uses Task Scheduler & AHK to unlock the system and let the video play without interruptions.
- **⚡ Simple Setup**: Easy to clone, configure, and use.

---

## 🛠️ Tech Stack

- **Python**: Core language for video and audio handling 🎞️
- **OpenCV**: For video playback control 📽️
- **Pygame**: Audio playback 🎶
- **PyInstaller**: Convert Python script to EXE 🔧
- **screeninfo**: Get screen size for centered video 📐
- **Task Scheduler**: Automate unlocking workstation 🔓
- **AutoHotkey (AHK)**: Simulate unlock on system startup 🖱️

---

## ⚡ Quick Setup

1. **Clone the Repo**:  
    Clone the project to your local machine:
    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the Project Directory**:  
    Change to the cloned project directory:
    ```bash
    cd <project_directory>
    ```

3. **Clean Up (Optional)**:  
    Remove unnecessary files for a clean setup:
    ```bash
    rm -rf .git build dist
    ```

4. **Update the Audio and Video Files**:  
    Replace `focus_video.mp4` and `focus_audio.mp3` with your own motivational video and audio files. If you prefer, you can continue using the existing ones.

5. **Install Dependencies**:  
    Install the required libraries:
    ```bash
    pip install opencv-python pygame screeninfo pyinstaller
    ```

6. **Update Video/Audio Paths in Script**:  
    Open the `focus_video_script.py` file and update the paths to your video and audio files.

7. **Convert Python to EXE**:  
    Use PyInstaller to convert the Python script into an EXE:
    ```bash
    pyinstaller --onefile --windowed focus_video_script.py
    ```

8. **Create Task Scheduler for Auto Unlock**:  
    Create a Task Scheduler job to run an AutoHotKey (AHK) script at login to unlock your system for the video:
    ```ahk
    ; AHK Script Example for unlocking the workstation
    SetTitleMatchMode, 2
    Loop {
         IfWinExist, Lock Screen
         {
              Send, {Enter}
              break
         }
         Sleep, 1000  ; Wait before checking again
    }
    ```

9. **Add EXE to Startup**:  
    Add the generated EXE to your Startup folder or configure Task Scheduler to run it at login:
    ```bash
    # Open Startup folder
    shell:startup
    ```

10. **Enjoy Focused Productivity**:  
    When you start your laptop, the motivational video will automatically play, helping you stay focused and productive! 🎯
---

## 💡 Learnings & Challenges

- Integrated Python libraries (OpenCV, Pygame) for seamless video & audio playback.
- Used PyInstaller to package the script into an EXE.
- Automated workstation unlock using Task Scheduler & AutoHotkey.
- Perfected the startup process for minimal distractions. 🔑

---

## 🛠️ Example AHK Script

```ahk
; AHK Script to unlock desktop when locked
#Persistent
SetTitleMatchMode, 2

Loop {
     IfWinExist, Lock Screen
     {
          Send, {Enter}
          break
     }
     Sleep, 1000  ; Wait before checking again
}
```

---

## 💬 Final Thoughts

This project is not only a personal solution but also a tool for anyone who struggles with distractions. It ensures a motivational start to the day, making you ready to focus and be productive! 🚀
