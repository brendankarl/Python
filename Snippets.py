#Sleep for 5 seconds
import time
time.sleep(5)

#Get/change current directory
import os
os.getcwd()
os.chdir('D:\\')

#Use the webbrowser module to open a new page
import webbrowser
webbrowser.open('https://www.bing.co.uk')

#Using the Pyperclip module
import pyperclip
pyperclip.paste()
pyperclip.copy('This is a test')