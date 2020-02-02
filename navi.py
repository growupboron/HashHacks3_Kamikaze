import os
from gtts import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(6,GPIO.IN)

os.chdir(os.getcwd()+'/book')

a=os.listdir()
print(a)
i=0
click=0
right=0
left=0
while(click!=1):
    tts =gTTS(text=a[i],lang='en')
    tts.save('file'+str(i)+'.mp3')
    os.system('mpg321 file'+str(i)+'.mp3')
    #print(click,"click before input")
    #print(click,"click before input")
    #print(click,"click before input")
    right=GPIO.input(6)
    left=GPIO.input(19)
    click=GPIO.input(16)
    #print(click,"click after input")
    #print(right,"right afer input")
    #print(left,"left after input")
    if(click):
        os.system("convert -density 300 "+a[i]+" -depth 8 -strip -background white -alpha off out.tiff")
        os.system("tesseract out.tiff text")
        import speech
    elif(right):
        i+=1
    elif (left):
        i-=1
    
b=os.listdir()
for x in a:
    b.remove(x)
for x in b:
    os.remove(x)
