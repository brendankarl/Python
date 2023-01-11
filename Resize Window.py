# pip install PyGetWindow
import pygetwindow

windows = pygetwindow.getAllTitles()

for window in windows:
    print(window)

edge = pygetwindow.getWindowsWithTitle("Untitled - Notepad")[0]
edge.resizeTo(1920, 1080)