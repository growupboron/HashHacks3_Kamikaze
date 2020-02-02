from gtts import *
import os
#
os.chdir('..')
print(os.getcwd())
import bin

#print(os.getcwd())
text_file = open("text.txt", "r")
lines = text_file.read().split('\r')
tts =gTTS(text=lines[0],lang='en')
tts.save('speech.mp3')

os.system("mpg321 speech.mp3")
