import RPi.GPIO as GPIO
import time
from RMove import Motion
from speak import Speak
from LED import Light

l=Light()
motion = Motion()

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT) #Motor 1 SF
GPIO.setup(6, GPIO.OUT) #Motor 2 SF
		
GPIO.setup(12, GPIO.OUT) #Motor 1 PMW
GPIO.setup(13, GPIO.OUT) #Motor 2 PMW
		
GPIO.setup(22, GPIO.OUT) #Motor 1 EN
GPIO.setup(23, GPIO.OUT) #Motor 2 EN

GPIO.setup(24, GPIO.OUT) #Motor 1 DIR
GPIO.setup(25, GPIO.OUT) #Motor 2 DIR

GPIO.setup(13, GPIO.OUT) #Motor1 PMW
GPIO.setup(12, GPIO.OUT) #Motor2 PMW

GPIO.setup(19, GPIO.OUT) #speaker

led1=20
led2=10
led3=9
led4=8
led5=11
led6=7

GPIO.setup(led1, GPIO.OUT) #LED 1
GPIO.setup(led2, GPIO.OUT) #LED 2
GPIO.setup(led3, GPIO.OUT) #LED 3
GPIO.setup(led4, GPIO.OUT) #LED 4
GPIO.setup(led5, GPIO.OUT) #LED 5
GPIO.setup(led6, GPIO.OUT) #LED 6


p2 = GPIO.PWM(13, 150)
p1 = GPIO.PWM(12, 150)

p2.start(10)      # left
p1.start(10)     # right

def onTone():            
    Speak.one(.1)
    Speak.two(.1)
    Speak.three(.1)
    Speak.four(.1)
    Speak.five(.1)

def onLed():
    l.led1(1)
    time.sleep(.1)
    l.led2(1)
    time.sleep(.1)
    l.led3(1)
    time.sleep(.1)
    l.led4(1)
    time.sleep(.1)
    l.led5(1)
    time.sleep(.1)
    l.led6(1)
    time.sleep(.1)

def offLed():
    l.led6(0)
    time.sleep(.1)
    l.led5(0)
    time.sleep(.1)
    l.led4(0)
    time.sleep(.1)
    l.led3(0)
    time.sleep(.1)
    l.led2(0)
    time.sleep(.1)
    l.led1(0)

def offTone():
    Speak.five(.1)
    Speak.four(.1)
    Speak.three(.1)
    Speak.two(.1)
    Speak.one(.1)


onTone()

onLed()

time.sleep(.3)

print('forward')
motion.forward(1)

print('backward')
motion.reverse(1)

print('Right')
motion.right_pivot(1)

print('left')
motion.left_pivot(1)

motion.stop()

p1.stop()
p2.stop()

time.sleep(.3)  

offTone()
offLed()

GPIO.cleanup()