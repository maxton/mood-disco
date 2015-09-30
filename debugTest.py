import pygame
import time
import RPi.GPIO as GPIO
import math
import json
import urllib
pygame.init()
pygame.mixer.init()


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


def moodcheck(IOB, EOC, LOH, HOS):
	if(HOS > .3):
		if(IOB > .3):
			print("MOOD: MOTIVATED");
			pygame.mixer.music.load('motivation.mp3')
			pygame.mixer.music.play(-1)
			R = 7;
			G = 45;
			B = 0;
		elif(IOB < -.3):
			print("MOOD: Lazy");
			pygame.mixer.music.load('lazy.mp3')
			pygame.mixer.music.play(-1)
			R = 32;
			G = 12;
			B = 54;
		elif(LOH > .3):
			print("MOOD: Romantic");
			pygame.mixer.music.load('romance.mp3')
			pygame.mixer.music.play(-1)
			R = 80;
			G = 0;
			B = 0;
		elif(LOH < -.3):
			print("MOOD: Evil");
			pygame.mixer.music.load('evil.mp3')
			pygame.mixer.music.play(-1)
			R = 80;
			G = 5;
			B = 9;
		elif(EOC > .3):
			print("MOOD: Gleeful");
			pygame.mixer.music.load('gleeful.mp3')
			pygame.mixer.music.play(-1)
			R = 100;
			G = 47;
			B = 0;
		elif(EOC < -.3):
			print("MOOD: Content");
			pygame.mixer.music.load('content.mp3')
			pygame.mixer.music.play(-1)
			R = 31;
			G = 78;
			B = 0;
		else:
			print("MOOD: Happy");
                        pygame.mixer.music.load('happy.mp3')
                        pygame.mixer.music.play(-1)
			R=67;
			G=66;
			B=9;
	elif(HOS < -.3):
		if(IOB > .3):
			print("MOOD: Distant");
			pygame.mixer.music.load('distant.mp3')
			pygame.mixer.music.play(-1)
			R = 0;
			G = 0;
			B = 100;
		elif(IOB < -.3):
			print("MOOD: Lonely");
			pygame.mixer.music.load('lonely.mp3')
			pygame.mixer.music.play(-1)
			R=86;
			G=0;
			B=86;
		elif(LOH>.3):
			print("MOOD: Melancholy");
			pygame.mixer.music.load('melancholy.mp3')
			pygame.mixer.music.play(-1)
			R=9;
			G=68;
			B=4;
		elif(LOH<-.3):
			print("MOOD: Vengeful");
			pygame.mixer.music.load('vengence.mp3')
			pygame.mixer.music.play(-10)
			R=100;
			G=0;
			B=0;
		elif(EOC>.3):
			print("MOOD: Bittersweet");
			pygame.mixer.music.load('bittersweet.mp3')
			pygame.mixer.music.play(-1)
			R=100;
			G=0;
			B=52;
		elif(EOC<-.3):
			print("MOOD: Ashamed");
			pygame.mixer.music.load('ashamed.mp3')
			pygame.mixer.music.play(-1)
			R=7;
			G=7;
			B=7;
		else:
			print("MOOD: Sad");
                        pygame.mixer.music.load('calm.mp3') 
                        pygame.mixer.music.play(-1)
			R=0;
			G=60;
			B=0;
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
			pygame.mixer.music.load('passionate.mp3')
			pygame.mixer.music.play(-1)
			R=66;
			G=0;
			B=0;
		elif(LOH<-.3):
			print("MOOD: Engrossed");
			pygame.mixer.music.load('engrossed.mp3')
			pygame.mixer.music.play(-1)
			R=0;
			G=15;
			B=62;
		elif(EOC>.3):
			print("MOOD: Attentive");
			pygame.mixer.music.load('attentive.mp3')
			pygame.mixer.music.play(-1)
			R=89;
			G=51;
			B=0;
		elif(EOC<-.3):
			print("MOOD: Focused");
			pygame.mixer.music.load('focused.mp3')
			pygame.mixer.music.play(-1)
			R=100;
			G=47;
			B=0;
		else:
			print("MOOD: Interested");
                        pygame.mixer.music.load('interested.mp3')
                        pygame.mixer.music.play(-1)

			R=0;
			G=28;
			B=50;
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
			pygame.mixer.music.load('mundane.mp3')
			pygame.mixer.music.play(-1)
			R=70;
			G=39;
			B=0;
		elif(LOH<-.3):
			print("MOOD: Lifeless");
			pygame.mixer.music.load('lifeless.mp3')
			pygame.mixer.music.play(-1)
			R=11;
			G=11;
			B=11;
		elif(EOC>.3):
			print("MOOD: Anticipation");
			pygame.mixer.music.load('anticipation.mp3')
			pygame.mixer.music.play(-1)
			R=70;
			G=39;
			B=0;
		elif(EOC<-.3):
			print("MOOD: Lazy");
			pygame.mixer.music.load('lazy.mp3')
			pygame.mixer.music.play(-1)
			R=23;
			G=23;
			B=23;
		else:
			print("MOOD: Bored");
                        pygame.mixer.music.load('bored.mp3')
                        pygame.mixer.music.play(-1)
			R=20;
			G=39;
			B=10;
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
			pygame.mixer.music.load('romance.mp3')
			pygame.mixer.music.play(-1)
			R=66;
			G=0;
			B=0;
		elif(EOC<-.3):
			print("MOOD: Content");
			pygame.mixer.music.load('content.mp3')
			pygame.mixer.music.play(-1)
			R=31;
			G=78;
			B=0;
		else:
			print("MOOD: Love");
                        pygame.mixer.music.load('love.mp3')
                        pygame.mixer.music.play(-1)
			R=99;
			G=8;
			B=59;
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
			pygame.mixer.music.load('evil.mp3')
			pygame.mixer.music.play(-1)
			R=90; 
			G=5;
			B=9;
		elif(EOC<-.3):
			print("MOOD: Passive Agressive");
			pygame.mixer.music.load('background.mp3')
			pygame.mixer.music.play(-1)
			R=100;
			G=78;
			B=40;
		else:
			print("MOOD: HATE");
                        pygame.mixer.music.load('hate.mp3')
                        pygame.mixer.music.play(-1)
			R=80;
			B=0;
			G=0;
	elif(EOC>.3):
		 print("MOOD: EXCITED");
                 pygame.mixer.music.load('excited.mp3')
                 pygame.mixer.music.play(-1)
                 R=0;
                 B=90;
                 G=12;
	elif(EOC<-.3):
		 print("MOOD: HATE");
                 pygame.mixer.music.load('calm.mp3')
                 pygame.mixer.music.play(-1)
                 R=0;
                 B=90;
                 G=12;
	else:
		pygame.mixer.music.load('background.mp3')
		pygame.mixer.music.play(-1)
		R=100;
		G=100;
		B=100;
	return(R,G,B);
try:
	while 1 == 1:
    		# R= input("colorX");
		# G= input("colorY");
		# B= input("colorZ");
		url='http://mood-dis.co/api/getCurrentMood?key=098f6bcd4621d373cade4e832627b4f6&avg_size=6'
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
			if(pp==0):
				p1=IOB;
				p2=EOC;
				p3=LOH;
				p4=HOS;
				pp=1;
			
			if(p1==IOB and p2==EOC and p3==LOH and p4==HOS):
				if(pygame.mixer.music.get_busy()):
					a=0;
				else:
					pygame.mixer.music.fadeout(500)
					[r,g,b]=moodcheck(IOB,EOC,LOH,HOS);
				time.sleep(2);
			else:
				print(str(IOB)+':'+str(EOC)+':'+str(LOH)+':'+str(HOS));

				[r,g,b]=moodcheck(IOB,EOC,LOH,HOS);
				colour(int(r), int(g), int(b), 4);
				time.sleep(2);
				pygame.mixer.music.fadeout(500)
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
