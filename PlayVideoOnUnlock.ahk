#Persistent
#NoEnv
SetTitleMatchMode, 2

; Path to the executable
exePath := "C:\Users\hp\Desktop\Video_startup\start_script.py"

; Register for session unlock event
OnMessage(0x2B1, "OnUnlock")

OnUnlock(wParam, lParam, msg, hwnd) {
    FileAppend, %A_Now% - Event Triggered: %wParam%`n, C:\Temp\debug.log ; Log the event
    if (wParam = 7) ; 7 indicates session unlock
    {
        MsgBox, Session Unlock Detected! Running the video...
        Run, %exePath%
    }
}
