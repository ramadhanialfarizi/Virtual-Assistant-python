# import tools
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

# Start pyttsx3 as a engine
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_App_ID')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

# Start Speaking
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

# Hour Fungtion
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 15:
        speak('Good Afternoon!')

    if currentH >= 15 and currentH < 18:
        speak('Good Evening!')

    if currentH >= 18 and currentH !=0:
        speak('good night!')

# Opening or Say
greetMe()

speak('Hello Sir, I am your digital assistant Karin. i think you need my help')
speak('what can i do for you?')

# Microphone Function
def myCommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I can\'t hear you! Try typing the command!')
        query = str(input('Command: '))

    return query
        
# Starting Assistant
if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()

# Task 1      
        if 'youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        
        elif 'bukalapak' in query:
            speak('okay')
            webbrowser.open('https://www.bukalapak.com/')

        elif 'tokopedia' in query:
            speak('okay')
            webbrowser.open('https://www.tokopedia.com/')

        elif 'gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'shopee' in query:
            speak('okay')
            webbrowser.open('https://shopee.co.id/')

        elif 'twitter' in query:
            speak('okay')
            webbrowser.open('https://twitter.com/')

        elif 'traveloka' in query:
            speak('okay')
            webbrowser.open('https://www.traveloka.com/id-id/')

        elif 'instagram' in query:
            speak('okay')
            webbrowser.open('https://www.instagram.com/?hl=id')
        
        elif 'documents' in query or "docs" in query:
            speak('okay')
            webbrowser.open('https://docs.google.com/document/u/0/')


# conversation
        elif 'hey' in query:
            speak('yes sir!')

        elif 'who are you' in query:
            speak ('im your digital assistent, i am ready to help you')
        
        elif 'your name' in query:
            speak('my name is karina, nice to meet you sir')

        elif' living' in query or'live' in query or' living now' in query:
            speak('i live in your device, you can call me anytime')

        elif'created' in query or 'create' in query:
            speak('im created by rama, he is my lord')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'thank you' in query or 'thank\'s' in query:
            speak('your welcome, i am happy to help you ')
            sys.exit()

# Task 2
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
                                    

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')