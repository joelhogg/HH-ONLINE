import time
import speech_recognition as sr
from gtts import gTTS
import os
import urllib.request
import json
from weather import Weather, Unit

class CurrencyConverter:

    rates = []
    
    def __init__(self,url):
        req = urllib.request.Request(url)
        data = urllib.request.urlopen(req).read()
        data = json.loads(data.decode('utf-8'))
        self.rates = data["rates"]

    def convert(self,amount, from_currency, to_currency):
        initial_amount = amount
        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]
        if to_currency == "EUR":
            return initial_amount, from_currency, '=', amount, to_currency
        else:
            return initial_amount, from_currency, '=', round(amount * self.rates[to_currency],2), to_currency

converter = CurrencyConverter("http://data.fixer.io/api/latest?access_key=4202c616ed8a0df8ee176544488d5560")

valid = False
while valid == False:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,timeout=2,phrase_time_limit=15)
#voice transcription
    try:
        print("Transcription: " + r.recognize_google(audio))
        vAudio = r.recognize_google(audio)
        vList = vAudio.split(" ")
        valid = True
    except sr.UnknownValueError:
        print("Audio is unintelligable")
        tts = gTTS(text="Audio is unintelligable", lang='en')
        tts.save("pcvoice.mp3")
        os.system("start pcvoice.mp3")
        time.sleep(5)
        valid = False
    except sr.RequestError as e:
        print("cannot obtain results; [0]", format(e))

vList = vAudio.split(" ")

if vList[0] == "convert":
    Var1 = int(vList[1])
    Var2 = str(vList[2].upper())
    Var3 = str(vList[4].upper())
    vFinal = (converter.convert(Var1, Var2, Var3))
    print(vFinal)
    tts = gTTS(text=str(vFinal), lang='en')
    tts.save("pcvoice.mp3")
    os.system("start pcvoice.mp3")
#elif vAudio == "this is so sad":
#    tts = gTTS(text="Tú, tú eres el imán y yo soy el metal", lang='es')
#    tts.save("pcvoice.mp3")
#    os.system("start pcvoice.mp3")
elif vAudio == "what time is it":
    vTime = (time.strftime("%H:%M"))
    print(vTime)
    tts = gTTS(text=vTime, lang='en')
    tts.save("pcvoice.mp3")
    os.system("start pcvoice.mp3")
elif vAudio == "what date is it":
    vDate = time.strftime("%y/%m/%d")
    print(vDate)
    tts = gTTS(text=vDate, lang='en')
    tts.save("pcvoice.mp3")
    os.system("start pcvoice.mp3")
elif vList[0] == "what" and vList[1] == "is" and vList[2] == "the" and vList[3] == "weather" and vList[4] == "in":
    vLocation = vList[5]
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(vLocation)
    condition = location.condition
    print(condition.text)
    vCondition = (condition.text)
    tts = gTTS(text=vCondition, lang='en')
    tts.save("pcvoice.mp3")
    os.system("start pcvoice.mp3")

    
                    
