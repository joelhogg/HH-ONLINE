import time
import speech_recognition as sr
from gtts import gTTS
import os

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
