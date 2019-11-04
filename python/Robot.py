import RPi.GPIO as GPIO
import time
from RMove import Motion

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT) #Motor 1 SF
GPIO.setup(6, GPIO.OUT) #Motor 2 SF
		
#GPIO.setup(12, GPIO.OUT) #Motor 1 PMW
#GPIO.setup(13, GPIO.OUT) #Motor 2 PMW
		
GPIO.setup(22, GPIO.OUT) #Motor 1 EN
GPIO.setup(23, GPIO.OUT) #Motor 2 EN

GPIO.setup(24, GPIO.OUT) #Motor 1 DIR
GPIO.setup(25, GPIO.OUT) #Motor 2 DIR

GPIO.setup(13, GPIO.OUT) #Motor1 PMW
GPIO.setup(12, GPIO.OUT) #Motor2 PMW

p = GPIO.PWM(13, 50)
p1 = GPIO.PWM(12, 0)

GPIO.setup(2, GPIO.IN)    # set GPIO2 as input (button)

p.start(10)      # left
p1.start(10)     # right
print("Motion initiallized")


motion = Motion()

def test():
    motion.forward()
    sleep(1)
    motion.backward()
    sleep(1)
    motion.stop()
    
def edge_detected(channel):
    pin_active = GPIO.input(channel)
    events.append(pin_active)
    if pin_active: # if port 2 == 1  
        # print ("Rising edge detected on 2")
        motion.forward()
    else:                  # if port 2 != 1  
        # print ("Falling edge detected on 2")
        motion.reverse()
        time.sleep(.3)
        motion.right_pivot()
        time.sleep(.5)
  

GPIO.add_event_detect(2, GPIO.BOTH, callback=edge_detected)

events = []
print('hello.')
time.sleep(30)


print('here is what happened:')
print(events)
print('goodbye.')
GPIO.cleanup()
