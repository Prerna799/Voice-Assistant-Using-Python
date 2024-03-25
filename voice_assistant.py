import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib  # designed to send an email using Gmail's SMTP server
import time

engine = pyttsx3.init('sapi5')              # Microsoft Speech API (SAPI5), which is a speech synthesis API developed by Microsoft for Windows platforms. pyttsx3 is a Python library that provides an interface to this API
voices = engine.getProperty('voices')       # This line retrieves a list of available voices that the TTS engine can use
engine.setProperty('voice',voices[1].id)    # This sets the voice property of the TTS engine to a specific voice

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")    
    
    speak("I am zira. Please tell me how may I help you")    

def takeCommand(): #imports the necessary module speech_recognition as sr
    #takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.7 # defines the length of silence (in seconds) that indicates the end of a phrase
        audio = r.listen(source,timeout=5)

    try :
        print("recognizing.....")  
        query = r.recognize_google(audio, language = 'en-in') # recognize the speech input using the Google Web Speech API 
        print("user said :",query)

    except exception as e: #The Exception class is a base class for all built-in exceptions in Python. This means that using except Exception as e: will catch most, if not all, exceptions that can occur in Python code.
        print("say that again please.....")
        return "none"
    return query    

def sendEmail(to,content): #smtplib package in use that is already installed in python. It helps in sending emails through google
    #need to enable less secure apps to make this work.....but now due to some security reasons we need to go to two-step-verification and from there copy the password
    server = smtplib.SMTP('smtp.gmail.com',587) #server address ('smtp.gmail.com') and port number (587) as arguments
    server.ehlo()  #server.ehlo() is like your script politely introducing itself and asking Gmail's server, "What cool stuff can you do?"
    server.starttls() #necessary when connecting to Gmail's SMTP server to ensure secure communication
    server.login('prernasharma0018@gmail.com','tvas arvp tkhs vrol')
    server.sendmail('prernasharma0018@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()  #coverted the command into lower character so that when we get the query is is matched by the links that we are giving in the logic if-else ladder

        #logic for executing tasks based on query
        
        if 'how are you' in query :
            speak("I am great!! what about you?")
            
        elif 'hello' in query or 'hey' in query or 'hi' in query:
            speak("hello!! How are you??")
            
        elif 'i am good' in query or 'i am fine' in query :
            speak("I am glad to hear that. how may I help you")
            
        elif 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","") #we remove the word wikipedia from the input string and search the rest pf the input
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            speak(results)
            print(results)
            speak("what else can do for you?")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("what else can do for you?")
    
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("what else can do for you?")

        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            speak("what else can do for you?")

        elif 'open vs code' in query :
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  
            speak("what else can do for you?")

        elif 'send email' in query :  
            try:
                speak("what should I write in email?")
                content = takeCommand() #takeCommand returns the input given by user through microphone in form of string 
                if 'nothing' in content:
                    speak("okay no email has been sent!!")
                    speak("what else can do for you?")
                else:    
                    to = "prenasahrma0018@gmail.com" # receiver's mail 
                    sendEmail(to,content)
                    speak("email has been sent!")
                    speak("what else can do for you?")
            except Exception as e:
                print(e)
                speak("sorry unable to send the email")   
                speak("what else can do for you?")       

        elif 'quit' in query or 'exit' in query :
            speak("the program is being terminated")
            exit()
            
        elif 'thankyou' in query:
            speak("I hope I was helpful to you!!")
            
        else:
            time.sleep(5) # Wait for 10 seconds
            speak("sorry I am not capable of doing what you want!!")
        