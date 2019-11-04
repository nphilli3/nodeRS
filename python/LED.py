import RPi.GPIO as GPIO
import time

class Light:
		
	def led1(self,t):
		GPIO.output(20, t)
		
	def led2(self,t):
		GPIO.output(10, t)
	
	def led3(self,t):
		GPIO.output(9, t)
		
	def led4(self,t):
		GPIO.output(8, t)
		
	def led5(self,t):
		GPIO.output(11, t)
		
	def led6(self,t):
		GPIO.output(7, t)