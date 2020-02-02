import RPi.GPIO as GPIO
import time

A=[1,1,1,1,1,1]


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

p=GPIO.PWM(17, 50)
q=GPIO.PWM(27, 50)
r=GPIO.PWM(22, 50)
s=GPIO.PWM(23, 50)
t=GPIO.PWM(24, 50)
u=GPIO.PWM(25, 50)


p.start(2.5)
q.start(2.5)
r.start(2.5)
s.start(2.5)
t.start(2.5)
u.start(2.5)

try:
    
    if (A[0]==1):

        p.ChangeDutyCycle(7.5)
        
        
    if (A[1]==1):
        q.ChangeDutyCycle(7.5)
        

    if (A[2]==1):
        r.ChangeDutyCycle(7.5)

    if (A[3]==1):
        s.ChangeDutyCycle(7.5)

    if (A[4]==1):
        t.ChangeDutyCycle(7.5)

    if (A[5]==1):
        u.ChangeDutyCycle(7.5)

    else:
        print ("0,0,0,0,0,0")
    GPIO.cleanup()

except KeyboardInterrupt:
    p.stop()
    q.stop()
    r.stop()
    s.stop()
    t.stop()
    u.stop()
    GPIO.cleanup()
