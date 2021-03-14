import pywhatkit
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import random
import pyjokes




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)#change to voices[1].id if you want female voice

def speak(voice):
    engine.say(voice)
    engine.runAndWait() #without this command, speech wouldnt be audible


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
    speak("ZEN at your service.")

def takeCommand():
    #it takes mic input from user and returns string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5) #helps to lower the noise levels 
        print("Listening...")
        r.pause_threshold = 1
        voice = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(voice, language='en-in')
        querysl = r.recognize_google(voice, language='sl-SL')
        print(f"User said: {query}\n") #user query will be printed
        querysl = takeCommand().lower()

        #easter egg for slovenian language
        if'ali znaš kaj povedati po slovensko' in querysl:
            speak('slovensko govorim zelo slabo')
        else:
            pass

    except Exception as e:
        
        return "None"
       
    return query



if __name__ == "__main__":
    greetMe()
    response_list = ['yes?', 'How may I help you Sir?', 'Sir?']
    mood_list = ['Im good', 'I dont feel good right now', 'Im doing amazing']
   
    while True:
        query = takeCommand().lower()
        #wake word is then, as it has problems with hearing ZEN
        if 'then' in query:
            #remove wakeword from query->useful for playing songs, searching wikipedia
            query = query.replace('then', '')

            #search wiki
            if 'search wikipedia for' in query :
                speak('Searching Wikipedia...')
                query = query.replace("search wikipedia for", "")
                results = wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            #opens youutube
            elif 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open("www.youtube.com")
            #opens google
            elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("www.google.com")
            #tells the time
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%I %M %p")
                speak(f"Sir, the time is {strTime}")
            #tells a joke
            elif 'tell me a joke' in query:
                speak(pyjokes.get_joke())
                speak("Do you want to hear another one?")
                query = takeCommand().lower()
                if 'yes i want to hear another one' in query:
                    speak(pyjokes.get_joke())
                    query = takeCommand().lower()
                else:
                    speak("Oh to bad, i had a really funny one")
            #mood
            elif 'how are you' in query:
                speak(random.choice(mood_list))
                speak('What about yourself?')
                query2 = takeCommand().lower()
                if "i'm good" or "i'm doing fine" or "i'm okay" in query2:
                    speak("Good to hear that")
                elif "i'm not feeling okay" or "i'm sick" in query2:
                    speak("Oh, tomorrow will be better")
            #plays youtube video (first on the page of search)
            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing' + song)
                pywhatkit.playonyt(song)
            #shutdown
            elif 'shut down' or 'shutdown' in query:
                speak("Signing out...")
                quit()
        else:
            pass



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tgrumerec@gmail.com', 'jebemtimater1')
    server.sendmail('tgrumerec@gmail.com', to, content)
    server.close()