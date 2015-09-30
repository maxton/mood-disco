import pygame
import time
import RPi.GPIO as GPIO
import math
import json
import urllib


GPIO.setmode(GPIO.BOARD)
red = 37  # pin numbers to match LED legs
pp=0;
green = 35
blue = 33
GPIO.setup(red, GPIO.OUT)  # setup all the pins
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100  # Hz

# setup all the colours
RED = GPIO.PWM(red, Freq)  # Pin, frequency
RED.start(0)  # Initial duty cycle of 0, so off
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

def colour(R, G, B, on_time):  # colour brightness range is 0 - 100
        RED.ChangeDutyCycle(R)
        GREEN.ChangeDutyCycle(G)
        BLUE.ChangeDutyCycle(B)
        time.sleep(on_time)

# turn everything off

while 1==1:
	r=input("R");
	g=input("G");
	b=input("B");
	print(r)
	print(g)
	print(b)
	colour(r,g,b,4);


