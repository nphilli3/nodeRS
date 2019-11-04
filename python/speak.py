import RPi.GPIO as GPIO
import time

class Speak:
		
        def one(self):
            speak = GPIO.PWM(19, 600)
            speak.start(99)
            time.sleep(self)
            speak.stop()
        
        def two(self):
            speak = GPIO.PWM(19, 800)
            speak.start(99)
            time.sleep(self)
            speak.stop()
        
        def three(self):
            speak = GPIO.PWM(19, 1000)
            speak.start(99)
            time.sleep(self)
            speak.stop()
        
        def four(self):
            speak = GPIO.PWM(19, 1200)
            speak.start(99)
            time.sleep(self)
            speak.stop()
        
        def five(self):
            speak = GPIO.PWM(19, 1400)
            speak.start(99)
            time.sleep(self)
            speak.stop()
            
        dict = {'1':one, '2':two, '3':three, '4':four, '5':five}
