import time
import RPi.GPIO as GPIO
import math
import json
import urllib

GPIO.setmode(GPIO.BOARD)
red = 37  # pin numbers to match LED legs
green = 35
blue = 33
GPIO.setup(red, GPIO.OUT)  # setup all the pins
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100  # Hz
q=0;
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


def moodcheck(IOB, EOC, LOH, HOS):
	if(HOS > .3):
		if(IOB > .3):
			print("MOOD: MOTIVATED");
			R = 0;
			G = 100;
			B = 0;
		elif(IOB < -.3):
			print("MOOD: Lazy");
			R = 23;
			G = 23;
			B = 23;
		elif(LOH > .3):
			print("MOOD: Romantic");
			R = 66;
			G = 0;
			B = 0;
		elif(LOH < -.3):
			print("MOOD: Evil");
			R = 54;
			G = 9;
			B = 9;
		elif(EOC > .3):
			print("MOOD: Gleeful");
			R = 100;
			G = 47;
			B = 0;
		elif(EOC < -.3):
			print("MOOD: Content");
			R = 31;
			G = 78;
			B = 0;
	elif(HOS < -.3):
		if(IOB > .3):
			print("MOOD: Distant");
			R = 0;
			G = 0;
			B = 100;
		elif(IOB < -.3):
			print("MOOD: Lonely");
			R=86;
			G=0;
			B=86;
		elif(LOH>.3):
			print("MOOD: Melancholy");
			R=100;
			G=0;
			B=100;
		elif(LOH<-.3):
			print("MOOD: Vengeful");
			R=100;
			G=0;
			B=0;
		elif(EOC>.3):
			print("MOOD: Bittersweet");
			R=100;
			G=0;
			B=52;
		elif(EOC<-.3):
			print("MOOD: Ashamed");
			R=7;
			G=7;
			B=7;
	elif(IOB>.3):
		if(HOS>.3):
			print("MOOD: UK1");
			R=0;
			G=0;
			B=100;
		elif(HOS<-.3):
			print("MOOD: UK2");
			R=86;
			G=0;
			B=86;
		elif(LOH>.3):
			print("MOOD: Passionate");
			R=66;
			G=0;
			B=0;
		elif(LOH<-.3):
			print("MOOD: Engrossed");
			R=0;
			G=15;
			B=62;
		elif(EOC>.3):
			print("MOOD: Attentive");
			R=0;
			G=15;
			B=62;
		elif(EOC<-.3):
			print("MOOD: Focused");
			R=100;
			G=47;
			B=0;
	elif(IOB<-.3):
		if(HOS>.3):
			print("MOOD: UK3");
			R=0;
			G=0;
			B=100;
		elif(HOS<-.3):
			print("MOOD: UL4");
			R=86;
			G=0;
			B=86;
		elif(LOH>.3):
			print("MOOD: Mundane");
			R=70;
			G=39;
			B=0;
		elif(LOH<-.3):
			print("MOOD: Lifeless");
			R=11;
			G=11;
			B=11;
		elif(EOC>.3):
			print("MOOD: Anticipation");
			R=70;
			G=39;
			B=0;
		elif(EOC<-.3):
			print("MOOD: Lazy");
			R=23;
			G=23;
			B=23;
	elif(LOH>.3):
		if(HOS>.3):
			print("MOOD: UK4");
			R=0;
			G=0;
			B=100;
		elif(HOS<-.3):
			print("MOOD: UK5");
			R=86;
			G=0;
			B=86;
		elif(IOB>.3):
			print("MOOD: UK6");
			R=66;
			G=0;
			B=0;
                elif(IOB<-.3):
			print("MOOD: UK7");
			R=0;
			G=15;
			B=62;
		elif(EOC>.3):
			print("MOOD: Romantic");
			R=66;
			G=0;
			B=0;
		elif(EOC<-.3):
			print("MOOD: Content");
			R=31;
			G=78;
			B=0;
	elif(LOH<-.3):
		if(HOS>.3):
			print("MOOD: UK8");
			R=0;
			G=0;
			B=100;
		elif(HOS<-.3):
			print("MOOD: UK9");
			R=86;
			G=0;
			B=86;
		elif(IOB>.3):
			print("MOOD: UK10");
			R=66;
			G=0;
			B=0;
		elif(IOB<-.3):
			print("MOOD: UK11");
			R=0;
			G=15;
			B=62;
		elif(EOC>.3):
			print("MOOD: Evil");
			R=54; 
			G=9;
			B=9;
		elif(EOC<-.3):
			print("MOOD: Passive Agressive");
			R=100;
			G=78;
			B=40;

	return(R,G,B);
try:
	while 1 == 1:
    		# R= input("colorX");
		# G= input("colorY");
		# B= input("colorZ");
		url='http://mood-dis.co/api/getCurrentMood?key=098f6bcd4621d373cade4e832627b4f6'
		result=json.load(urllib.urlopen(url))
		success=result.items()[2];
		if(success[1]=='success'):
        		print('Rock and Roll');
        		data=result.items()[1];
        		data=data[1];
        		data=str(data).split(':',5)
        		str1=data[1];
        		str2=data[2];
        		str3=data[3];
        		str4=data[4];
        		IOB=float(str1[1:str1.index(',')]);#Interested or Bored
        		EOC=float(str2[1:str2.index(',')]);#Excited or Calm
        		LOH=float(str3[1:str3.index(',')]);#Love or Hate
        		HOS=float(str4[1:str4.index('}')]);#Happy or Sad
			
			if(q==0):
				p1=0;	
				p2=0;
				p3=0;
				p4=0;
			if(p1==IOB and p2==EOC and p3==LOH and p4==HOS):
				a=0;			
			else:
				print(str(IOB)+':'+str(EOC)+':'+str(LOH)+':'+str(HOS));
				[R,G,B]=moodcheck(IOB,EOC,LOH,HOS);
				colour(int(R), int(G), int(B), 4);

			p1=IOB;
			p2=EOC;
			p3=LOH;
			p4=HOS;
except KeyboardInterrupt:
    	pass

RED.stop()
GREEN.stop()
BLUE.stop()
GPIO.cleanup()
