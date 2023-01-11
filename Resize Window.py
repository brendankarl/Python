# pip install PyGetWindow
import pygetwindow

# Get all of the currently opened windows
windows = pygetwindow.getAllTitles()

# Print a list of the currently opened windows
for window in windows:
    print(window)

# Specify the name of the window to resize
notepad = pygetwindow.getWindowsWithTitle("Untitled - Notepad")[0]

#resize the window
notepad.resizeTo(1920, 1080)
