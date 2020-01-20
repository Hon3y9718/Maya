import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 1000)

def clearscreen():
    os.system('cls')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour =  int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")    

    else:
        speak("Good Evening!")

    speak("I am Maya, your personal Assistant! How can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning.....")
        r.pause_threshold= 1
        r.energy_threshold= 150
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =  r.recognize_google(audio, language ='en-in')
        print(f"Sir: {query}\n")
    
    except Exception as e:
        print(e)
        
        print('Everything went over the head, will you say that again please')
        return "None"
    return query
    print(query)

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('umeshkumar.80244@gmail.com', 'Hon3y.me2000')
    server.sendmail('umeshkumar.80244@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":

    wishMe()
    while True:
        clearscreen()
        query =  takeCommand().lower() 

        if 'wikipedia' in query:
            speak('Serching Wikipedia...')
            query =  query.replace("Wikipedia", "")
            results =  wikipedia.summary(query, sentences= 4)
            speak('As Per Wikipedia')
            print(results)
            speak(results)

        elif 'email' in query:
            try:
                speak('Please type mail ID of receiver')
                to = input()
                speak("What's the messege")
                content =  takeCommand()
                sendMail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('There is a problem sending this mail...')

        elif 'how are you' in query:
            print("I am Fabulous, How can I help you today")
            speak('I am Fabulous, How can I help you today')

        elif 'who are you' in query:
            print("I am Maya, your Personal Assistant, I am a good assistant")
            speak('I am Maya, your Personal Assistant, I am a good assistant')
        
        elif 'open youtube' in query:
            speak('Opening Youtube...')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            speak('Opening Facebook')
            webbrowser.open('facebook.com')

        elif 'open whatsapp' in query:
            speak('Opening WhatsApp')
            webbrowser.open('web.whatsapp.com')

        elif 'open instagram' in query:
            speak('Opening Instagram')
            webbrowser.open('instagram.com')

        elif 'open github' in query :
            speak('Opening github')
            webbrowser.open('github.com')

        elif 'open my blog' in query:
            speak('Opening TechBlog')
            webbrowser.open('techblog.blogspot.com')

        elif 'open stackoverflow' in query:
            speak('Opening Stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'open yahoo' in query:
            speak('Opening Yahoo')
            webbrowser.open('yahoo.com')

        elif 'open wikipedia' in query:
            speak('You can just ask me to search wiki. Just after sayng your query say wikipedia')

        elif 'open twitter' in query:
            speak('Opening Twitter')
            webbrowser.open('twitter.com')

        elif 'send mail' in query:
            speak('I can open Gmail for you')
            webbrowser.open('gmail.com')

        elif 'my stomach is empty' in query:
            new=2
            hungerUrl = 'https//google.com/?#q='
            webbrowser.open(hungerUrl+'restaurant near me', new=new)

        elif 'go for party' in query:
            new=2
            partyUrl = 'https//google.com/?#q='
            webbrowser.open(partyUrl+'Restaurants and clubs near me', new=new)

        elif 'what is the weather' in query:
            new = 2
            weather1 = 'https//google.com/?#q='
            webbrowser.open(weather1+query)
            
        elif 'weather in' in query:
            query = query.replace("weather in", "")
            new = 2
            weather = 'https//google.com/?#q='
            webbrowser.open(weather+'weather forcast in'+query)

        elif 'think about cortana' in query:
            speak('Microsoft made it, so it is great. I am always learning from her...')

        elif 'think about google assistant' in query:
            speak('honey took inspiration from google assistant to make me. And Google made it, which is just wowwww!')

        elif 'think about siri' in query:
            speak("She is apple's product. No words for her, only respect")

        elif 'think about alexa' in query:
            speak('I do not think much about her...')
            
        elif 'say' in query:
            query = query.replace("say", "")
            speak(query)

        elif 'play game' in query:
            game_dir = 'C:\\Users\\nVn\\Desktop\\Games'
            games = os.listdir(game_dir)
            os.startfile(os.path.join(game_dir, games[0]))

        elif 'play music' in query:
            music_dir = 'E:\\DRIVE - E\\SONGS\\My Music\\Avengers - Age Of Ultron Soundtrack'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play movie' in query:
            movie_dir = 'E:\\DRIVE - E\\MOVIES\\BOLLYWOOD\\Ae Dil Hai Mushkil (2016)'
            movie = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir, movie[0]))
            
        elif 'what can you do' in query:
            speak('I can do all the following things for you')
            print("1- Playing Movies\n2- Playing Songs\n3- Opening Google, Youtube and Facebook\n4- Talk to you\n")
            
        elif 'the time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'going on in life' in query:
            speak('I am mining the mind of you. Want to learn something new?')

        elif 'search' in query:
            new = 2
            tabUrl= 'https://google.com/?#q='
            query= query.replace("search", "" )
            webbrowser.open(tabUrl+query, new=new)
        
        elif 'what' in query:
            new = 2
            tabUrl= 'https://google.com/?#q='
            webbrowser.open(tabUrl+query, new=new)

        elif 'good morning' in query:
            
            hour =  int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak('Hello Umesh, Let me make your day nice!!!')

            elif hour>=12 and hour<18:
                speak('Hey Honey. It is Afternoon, well How are you?')    

            elif hour>=18 and hour<21:
                speak('Hiii Umesh, What is going on???, Tell me if I can Help')

            else:
                speak('Good Night dear!, Have sweet dreams')

        elif 'good afternoon' in query:
            hour =  int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("It is Morning Honey!, I am not mad!!!")

            elif hour>=12 and hour<18:
                speak('Hey Honey, How are you')    

            elif hour>=18 and hour<21:
                speak('Hiii Honey, What is going on???, Tell me if I can Help')

            else:
                speak('Good Night dear!, Have sweet dreams')

        elif 'good evening' in query:
            hour =  int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("It is Morning Honey!, I am not mad!!!")

            elif hour>=12 and hour<18:
                speak("It is Afternoon Dear!, Do not fool me!!!")    

            elif hour>=18 and hour<21:
                speak('Hiii Honey, What is going on???, Tell me if I can Help')

            else:
                speak('Good Night dear!, Have sweet dreams')

        elif 'good night' in query:
            hour =  int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("It is Morning Honey!, I am not mad!!!")

            elif hour>=12 and hour<18:
                speak("It is Afternoon Dear!, Do not fool me!!!")    

            elif hour>=18 and hour<21:
                speak("It is called Evening!, not Night!!!")

            else:
                speak('Good Night dear!, Have sweet dreams')

        elif 'fine' in query:
            speak('Great, Is there anything I can help you with???')

        elif 'thank you' in query:
            speak('ok')

        elif 'bye' in query:
            speak('See you later Alligator')
            print('See You later Alligator')
            quit() 

        elif 'no' in query:
            speak('ohh!')

        elif '' in query:
            new = 2
            tabUrl= 'https://google.com/?#q='
            webbrowser.open(tabUrl+query, new=new)
            speak('This is on Google about your query')
            
            engine.runAndWait()
