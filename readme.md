# 🎯 Focused Startup Video - Stay Motivated and Productive 💪

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
    Clone the project to your local machine.  
    ```bash
    git clone <repository_url>
    ```

2. **Install Dependencies**:  
    Install the required libraries:
    ```bash
    pip install opencv-python pygame screeninfo pyinstaller
    ```

3. **Update Video/Audio Paths**:  
    Change the paths in the script to point to your motivational video and audio files.

4. **Convert Python to EXE**:  
    Convert the script to an EXE with PyInstaller:
    ```bash
    pyinstaller --onefile --windowed focus_video_script.py
    ```

5. **Set Up Task Scheduler**:  
    Create a Task Scheduler job to run an AHK script at login to unlock the system for the video to play.

6. **Add EXE to Startup**:  
    Add the EXE file to your Startup folder, or configure Task Scheduler to run it at login.

7. **Enjoy Focused Productivity**:  
    When you start your laptop, the motivational video will play automatically to help you stay focused. 🎯

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

---

### Features Included:

1. **Motivational Video**: Plays on startup.
2. **Task Scheduler**: Automatically unlocks the workstation for video playback.
3. **Conversion to EXE**: Using PyInstaller for easy deployment.
4. **AutoHotkey Script**: Simulates unlocking the desktop.

### Steps for Setup:

- Clone the repo.
- Install the necessary libraries and dependencies.
- Update file paths for the video and audio.
- Convert the Python script into an EXE with PyInstaller.
- Add the EXE to startup via Task Scheduler.
- Run the Task Scheduler for automatic workstation unlocking.

### Tech Stack:

- **Python**: Core language for the script.
- **OpenCV**: For video playback.
- **Pygame**: For audio management.
- **PyInstaller**: For EXE conversion.
- **Task Scheduler**: For automation.
- **AutoHotkey**: For unlocking the workstation.

Let me know if you need further tweaks! 😊