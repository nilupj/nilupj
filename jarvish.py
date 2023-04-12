import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am jarvis sir. Please tell me how may i help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail', 587)
    server.ehlo()
    server.starttls()
    server.login('nirvaybehara@gmail.com', 'nirvay777@')
    server.sendmail('nirvaybehara@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\nirvay\\Desktop\\nirvay things\\audio song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%s")
            speak(f"sir, the time is {strTime}")            
        elif 'open code' in query:
            codePath = "c:\\User\\Haris\\AppData\\Local\\Programs\\Microsoft vs code\\code.exe"
            os.startfile(codePath)
        elif 'email to nirvay' in query:
            try:
                speak("what shoud i say?")
                content = takeCommand()
                to = "nirvaybehara@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend nirvay bhai.i am not able to send this email")