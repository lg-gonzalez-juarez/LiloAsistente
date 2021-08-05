# basado en https://www.youtube.com/watch?v=8WKjX0dbh4E

# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio
# paquete especial de audio
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
#pip install pywhatkit
#pip install wikipedia

import pyttsx3
import speech_recognition as sr
import pywhatkit

def talk(text):
    engine.say(text)
    engine.runAndWait()


name = 'Lilo'

listener=sr.Recognizer()
engine= pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

engine.say("Hola Lore")
engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando ...")
            voice = listener.listen(source)
            rec=listener.recognize_google(voice)
            rec=rec.lower()
            if name in rec:
                rec=rec.replace(name,'')
                print(rec)
                #talk(rec)
    except:
        pass
    return rec

def run():
    rec= listen()
    if 'reproduce' in rec:
        music=rec.replace('reproduce','')
        #print("reproduciendo")
        #talk(rec)
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)

run()