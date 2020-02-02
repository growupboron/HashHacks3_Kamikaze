import os
from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
p1=Servo(18)
q1=Servo(22)
r1=Servo(23)
s1=Servo(24)
t1=Servo(25)
u1=Servo(27)


braille = {
   '!': '001110',
   '?': '001011',
   '.': '001101',
   ';': '001010',
   ':': '001100',
   '-': '000011',
   ',': '001000',
   "’": '000010',
   '"': '000100',
   ' ': '000000',
   'a': '100000',
   'b': '101000',
   'c': '110000',
   'd': '110100',
   'e': '100100',
   'f': '111000',
   'g': '111100',
   'h': '101100',
   'i': '011000',
   'j': '011100',
   'k': '100010',
   'l': '101010',
   'm': '110010',
   'n': '110110',
   'o': '100110',
   'p': '111010',
   'q': '111110',
   'r': '101110',
   's': '011010',
   't': '011110',
   'u': '100011',
   'v': '101011',
   'w': '011101',
   'x': '110011',
   'y': '110111',
   'z': '100111',
   '1': '100000',
   '2': '101000',
   '3': '110000',
   '4': '110100',
   '5': '100100',
   '6': '111000',
   '7': '111100',
   '8': '101100',
   '9': '011000',
   '0': '011100',
   '#':'010111',
   
}
os.chdir(os.getcwd()+'/book')
text_file = open("text.txt", "r")
lines = text_file.read().split(' ')
mystr=''
lines=[s.replace('\n', mystr) for s in lines]
lines=[x+' ' for x in lines]

print (lines)
i=0
a=[]
while(i<len(lines)):
    len1=len(lines[i])
    j=0
    while(j<len1):
        ch=lines[i][j]
        ch=str.lower(ch)
        if(ch!='('and ch!=')'and ch!='‘'and ch!='|'and ch!='”'and ch!='“'and ch!='«'and ch!='\x0c'):
            a.append(list(map(int,braille[str(ch)])))    
        if(ch.isnumeric()):
            a.append(list(map(int,braille['#'])))
            a.append(list(map(int,braille[str(ch)])))            
        j=j+1
    i=i+1
print(a)
for x in a:
    #print("inside for")
    print(x)

    if(x[0]==1):
        #print("first if")
        
        p1.max()
        #sleep(1)
    if(x[1]==1):

        
        q1.max()
        #sleep(1)

    if(x[2]==1):
        r1.max()
        #sleep(1)

    if(x[3]==1):
        
        #s1.max()
        sleep(1)

    if(x[4]==1):
        
        t1.max()
        #sleep(1)

    if(x[5]==1):
        
        u1.max()
        #sleep(1)

    sleep(1)
    p1.mid()
    q1.mid()
    r1.mid()
    s1.mid()
    t1.mid()
    u1.mid()
print("end of bin")

