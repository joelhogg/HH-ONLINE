import time
import speech_recognition as sr
from gtts import gTTS
import os
import urllib.request
import json
from weather import Weather, Unit
import sys

class CurrencyConverter:

    rates = []
    
    def __init__(self,url):
        req = urllib.request.Request(url)
        data = urllib.request.urlopen(req).read()
        data = json.loads(data.decode('utf-8'))
        self.rates = data["rates"]

    def convert(self,amount, from_currency, to_currency):
        try:
            initial_amount = amount
            if from_currency != "EUR":
                amount = amount / self.rates[from_currency]
            if to_currency == "EUR":
                return initial_amount, from_currency, '=', amount, to_currency
            else:
                return initial_amount, from_currency, '=', round(amount * self.rates[to_currency],2), to_currency
        except:
            return "I cannot do that"

converter = CurrencyConverter("http://data.fixer.io/api/latest?access_key=4202c616ed8a0df8ee176544488d5560")

valid = False
while valid == False:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,phrase_time_limit=8)
        if audio == (""):
            valid = False
#voice transcription
    try:
        vAudio = r.recognize_google(audio)
        vList = vAudio.split(" ")
        valid = True
    except sr.UnknownValueError:
        tts = gTTS(text="Audio is unintelligable", lang='en')
        tts.save("pcvoice.mp3")
        os.system("start pcvoice.mp3")
        time.sleep(3)
        os.startfile("F:\Python\hogghomestartup.wav")
        time.sleep(1)
        valid = False
    except sr.RequestError as e:
        print("cannot obtain results; [0]", format(e))
        valid = False



vList = vAudio.split(" ")
print(vList)
if vList[0] == "convert":
    try:
        Var1 = int(vList[1])
        Var2 = str(vList[2].upper())
        Var3 = str(vList[4].upper())
        vFinal = (converter.convert(Var1, Var2, Var3))
        print(vFinal)
        tts = gTTS(text=str(vFinal), lang='en')
        tts.save("pcvoice.mp3")
        os.system("start pcvoice.mp3")
        time.sleep(7)
        os.system(r'"F:\Python\activate test 2.py"')
        exit()
    except:
        tts = gTTS(text="Sorry, i cant do that", lang='en')
        tts.save("pcvoice.mp3")
        os.system("start pcvoice.mp3")
        time.sleep(2)
        os.system(r'"F:\Python\activate test 2.py"')
        exit()

elif vAudio == "stop":
    os.system(r'"F:\Python\activate test 2.py"')
    exit()
    
elif vAudio == "this is so sad":
    os.startfile("F:\Python\Luis Fonsi - Despacito ft. Daddy Yankee (64  kbps).mp3")
    time.sleep(281)
    os.system(r'"F:\Python\activate test 2.py"')
    exit()

elif vAudio == "default":
    os.startfile("F:\Python\Fortnite Default Dance Ear Rape.mp3")
    time.sleep(7)
    os.system(r'"F:\Python\activate test 2.py"')
    exit()


else:
    os.system(r'"F:\Python\activate test 2.py"')

    exit()



        





























