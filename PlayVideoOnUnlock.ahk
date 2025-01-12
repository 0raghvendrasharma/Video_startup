#Persistent
#NoEnv
SetTitleMatchMode, 2

; Path to your executable
exePath := "C:\Users\hp\Desktop\Video_startup\dist\start_script.exe"

; Ensure the log directory exists and create an initial log entry
FileCreateDir, C:\Temp
FileAppend, Script started at %A_Now%`n, C:\Temp\debug.log

; Register for session unlock and system wake events
OnMessage(0x2B1, "HandleEvent") ; WM_WTSSESSION_CHANGE
OnMessage(0x0219, "HandleEvent") ; WM_DEVICECHANGE

HandleEvent(wParam, lParam, msg, hwnd) {
    ; Log every event for debugging
    FileAppend, %A_Now% - Event received. Msg: %msg%, wParam: %wParam%, lParam: %lParam%`n, C:\Temp\debug.log

    ; Detect unlock and wake scenarios
    if (msg = 0x2B1 && wParam = 7) || msg = 0x0219 {
        FileAppend, %A_Now% - Unlock/Wake detected. Attempting to run executable.`n, C:\Temp\debug.log
        try {
            Run, %exePath%
            FileAppend, %A_Now% - Executable ran successfully.`n, C:\Temp\debug.log
        } catch e {
            FileAppend, %A_Now% - Error running executable: %e%`n, C:\Temp\debug.log
            MsgBox, Error running the video: %e%
        }
    }
    return
}

; Immediate test option
MsgBox, 4, Test Run, Would you like to test run the video executable now?
IfMsgBox Yes
{
    Run, %exePath%
    FileAppend, %A_Now% - Manual test execution attempted`n, C:\Temp\debug.log
}
