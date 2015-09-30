import os
import time
import speech_recognition as sr
# obtain path to "test.wav" in the same folder as this script
import urllib2
from os import path
while 1==1:
    execfile('record.py')
    WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")

    # use "test.wav" as the audio source
    r = sr.Recognizer()
    with sr.WavFile(WAV_FILE) as source:
        audio = r.record(source) # read the entire WAV file

    # recognize speech using Google Speech Recognition
    #try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
    #    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    #except sr.UnknownValueError:
    #    print("Google Speech Recognition could not understand audio")
    #except sr.RequestError:
    #    print("Could not request results from Google Speech Recognition service")

    IBM_USERNAME = "22e85e08-a132-46ab-923f-3c2192f80e57" # IBM Speech to Text usernames are strings of the form X$
    IBM_PASSWORD = "CiXho4tj9f9g" # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError:
        print("Could not request results from IBM Speech to Text service")
    x=r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    y=x.split();

    for q in range(0, len(y)):
            print(y[q])
            urllib2.urlopen('http://54.210.194.0/api/addWord?key=098F6BCD4621D373CADE4E832627B4F6&word='+y[q])
    time.sleep(1)
    print(chr(27) + "[2J");
    print("PREPARE FOR SPEECH IN 2 SECONDS");
    time.sleep(2);
