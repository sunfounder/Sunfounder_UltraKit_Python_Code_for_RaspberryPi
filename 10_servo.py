#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

SigPin = 11
T = 0.02  #0.02s, 50HZ

pluse_width = [0.0005, 0.0010, 0.00125, 0.0015, 0.00175, 0.0020, 0.0025] #0,45,68,90,112,135,180

def set_angle(angle):
	GPIO.output(SigPin, GPIO.HIGH)
	time.sleep(angle)
	GPIO.output(SigPin, GPIO.LOW)
	time.sleep(T-angle)

def setup():
	GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location
	GPIO.setup(SigPin, GPIO.OUT)   #set pin mode is output
	GPIO.output(SigPin, GPIO.LOW) #set pin high level(3.3V)

def loop():
	while True:
		set_angle(pluse_width[0])
		time.sleep(0.5)
		set_angle(pluse_width[1])
		time.sleep(0.5)
		set_angle(pluse_width[2])
		time.sleep(0.5)
		set_angle(pluse_width[3])
		time.sleep(0.5)
		set_angle(pluse_width[4])
		time.sleep(0.5)

def destroy():   #When program ending, the function is executed. 
	GPIO.output(SigPin, GPIO.LOW)
	GPIO.setup(SigPin, GPIO.IN)   #set pin mode is input
'''
def ctrl(angle):
	n = 50
	while n:
		n = n - 1
		setup()
		if angle == 0:
			set_angle(0.0005)
		elif angle == 45:
			set_angle(0.0010)
		elif angle == 68:
			set_angle(0.00125)
		elif angle == 90:
			set_angle(0.0015)
		elif angle == 112:
			set_angle(0.00175)
		elif angle == 135:
			set_angle(0.0020)
		elif angle == 180:
			set_angle(0.0025)
		destroy()  
'''
if __name__ == '__main__':   #Program start from here 
	setup() 
	try:
		loop()  
	except KeyboardInterrupt:  
		destroy()  

