import RPi.GPIO as GPIO
import time

class Motion:
		
	def forward(self,t):
		GPIO.output(22, 1) #EN right
		GPIO.output(24, 1) #DIR right
		GPIO.output(23, 1) #EN Left 
		GPIO.output(25, 1) #Dir Left
		time.sleep(t)
		
	def right_pivot(self,t):
		GPIO.output(22, 1)
		GPIO.output(24, 0)
		GPIO.output(23, 1)
		GPIO.output(25, 1)
		time.sleep(t)

	def right_arch(self,t):
		GPIO.output(22, 0)
		GPIO.output(24, 0)
		GPIO.output(23, 0)
		GPIO.output(25, 0)
		time.sleep(t)
		
	def left_arch(self,t):
		GPIO.output(22, 0)
		GPIO.output(24, 0)
		GPIO.output(23, 0)
		GPIO.output(25, 0)
		time.sleep(t)

	def reverse(self,t):
		GPIO.output(22, 1)
		GPIO.output(24, 0)
		GPIO.output(23, 1)
		GPIO.output(25, 0)
		time.sleep(t)

	def left_pivot(self,t):
		GPIO.output(22, 1)
		GPIO.output(24, 1)
		GPIO.output(23, 1)
		GPIO.output(25, 0)
		time.sleep(t)

	def stop(self):
		GPIO.output(22, 0)
		GPIO.output(24, 0)
		GPIO.output(23, 0)
		GPIO.output(25, 0)
		
