import speech_recognition as sr
import os

valid = False
while valid == False:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source,timeout=60,phrase_time_limit=1)

        try:
            vAudio = r.recognize_google(audio)
            vAudio = vAudio.upper()
            vList2 = vAudio.split(" ")
            if len(vList2) == 2:
                if vList2[0] == ("OK" or "OKAY"):
                    if vList2[1] == "HOMEWORK":
                        os.startfile("F:\Python\hogghomestartup.wav")
                        os.system(r'"F:\Python\reWrite.py"')
                        exit()
                        valid = True
                    else:
                        valid = False
                else:
                   valid = False

        except sr.UnknownValueError:
                print("Audio is unintelligable")
                Valid = False

        except sr.RequestError as e:
            print("cannot obtain results; [0]", format(e))
