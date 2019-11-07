
import RPi.GPIO as GPIO
import requests
import time
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.IN)
URL = "http://localhost:1880/test"

try:  
    while True: 
        if GPIO.input(18):
            r = requests.post(URL, data ={'key':'value'})  
            print ("request sent")
                  
        else:  
            print ("Waiting input")  
           
        time.sleep(0.3)           
  
finally:                     
    GPIO.cleanup() 
 

