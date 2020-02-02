import RPi.GPIO as GPIO
import time

A=[1,0,1,0,0,0]


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

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
        while True:
                print("1")
                p.ChangeDutyCycle(5.0)
                q.ChangeDutyCycle(5.0)
                r.ChangeDutyCycle(5.0)
                s.ChangeDutyCycle(5.0)
                t.ChangeDutyCycle(5.0)
                u.ChangeDutyCycle(5.0)
                time.sleep(1)

                p.ChangeDutyCycle(7.5)
                q.ChangeDutyCycle(7.5)
                r.ChangeDutyCycle(7.5)
                s.ChangeDutyCycle(7.5)
                t.ChangeDutyCycle(7.5)
                u.ChangeDutyCycle(7.5)
                time.sleep(1)
                
                p.ChangeDutyCycle(10)
                q.ChangeDutyCycle(10)
                r.ChangeDutyCycle(10)
                s.ChangeDutyCycle(10)
                t.ChangeDutyCycle(10)
                u.ChangeDutyCycle(10)
                time.sleep(1)
                
                p.ChangeDutyCycle(12.5)
                q.ChangeDutyCycle(12.5)
                r.ChangeDutyCycle(12.5)
                s.ChangeDutyCycle(12.5)
                t.ChangeDutyCycle(12.5)
                u.ChangeDutyCycle(12.5)
                time.sleep(1)

                p.ChangeDutyCycle(15)
                q.ChangeDutyCycle(15)
                r.ChangeDutyCycle(15)
                s.ChangeDutyCycle(15)
                t.ChangeDutyCycle(15)
                u.ChangeDutyCycle(15)
                time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
