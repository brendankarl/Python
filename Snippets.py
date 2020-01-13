#Sleep for 5 seconds
import time
time.sleep(5)

#Get/change current directory
import os
os.getcwd()
os.chdir('D:\\')

#List files/folders
import os
os.chdir('D:\\')
print(os.getcwd())
files = os.listdir(os.getcwd())
for file in files:
    print(file)

#Use the webbrowser module to open a new page
import webbrowser
webbrowser.open('https://www.bing.co.uk')

#Using the Pyperclip module
import pyperclip
pyperclip.paste()
pyperclip.copy('This is a test')

#String formatting
age = 38
gender = "male"
text = "my age is {a}, my gender is {g}".format(a=age,g=gender)
print(text)

text = "my age is {0}, my gender is {1}".format(age,gender) #using different placeholder values
print(text)