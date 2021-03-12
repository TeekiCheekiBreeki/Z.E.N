import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import osimport smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voice[0].id)#change to voice[1].id if you want female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #without this command, speech wouldnt be audible


def wishme():
    hour = int(datetime.datetime.now().hour)

def takeCommand():
    #it takes mic input from user and returns string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
            print("Recognizing...")
            query = r.recognize_google(audio, language ='en-in') #using google recognition
            print(f"User said: {query}\n")#user query will be printed
        except Exception as e:
            #print(e)
            print("Say that again please...")
            return "None"
        return query
def main():
    speak("Hello Tian, my name is jarvis!")