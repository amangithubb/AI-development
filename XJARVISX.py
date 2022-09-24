import email
import queue
from time import time
from typing import Counter
from xmlrpc.client import _datetime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import os
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
        
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir")
        
    else:
        speak("Good Evening Sir")
        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amanswaroop2113@gmail.com', 'SAREGAMA_padha')
    server.sendmail('amanswaroop2113@gmail.com', to, content)
    server.close()       

def takeCommand():
# It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold= 300
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"   
    return query
   
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # query = input("You: ").lower()  
        print("You: ",query)
  
    #Logic for executing tasks based on query (51)
        if 'quit' in query:
            speak("Have a good day sir")
            quit()    
        elif 'open my folder' in query:
            speak("Opening your nuclear reactive foler...")
            os.startfile("C://Users//Anand swaroop//Desktop//Aman Python Projects")
        elif 'open movies' in query:
            speak("Opening movies...")
            os.startfile("C://Users//Anand swaroop//Desktop//Movies")
        elif 'press' in query:
            #key = input()
            speak("Which key you want to press")
            key = takeCommand()
            keyboard.press(key)
            speak("Executed !!")
        elif 'press and hold' in query:
            query = query.replace("press and hold","")
            keyboard.press_and_release(query)
            speak("Executed !!")
        elif 'send email' in query:
            
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should I send")
                to = input()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")
        elif 'you may rest' in query:
            speak('thanks')
            quit()
        elif "introduce yourself" in query:
            speak("I am JARVIS\nI am an AI, created by the great, scientist Aman Swaroop\nI can perform several functions\nJust say, What can you do")
        elif "morning" in query:
            speak("Good Morning Sir")
        elif "afternoon" in query:
            speak("Good Afternoon Sir")
        elif "night" in query:
            speak("Good Night and Stweet Dreams Sir")
        elif "hello" in query:
            speak("Hello Sir")
        elif "who are you" in query:
            speak("I am Jarvis Assistant Sir")  
        elif "how are you" in query:
            speak("I am fine , How can I help you?")
        elif "what is your name" in query:
            speak("I am jarvis assistant")   
        elif "what's the time" in query:
            strtime = datetime.datetime.now()
            speak(strtime)
        elif "open paint" in query:
            webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\paint")
            speak("Opening Paint")
        elif "open notepad" in query:
            webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories/notepad")
            speak("Opening Notepad")
        elif "open visual basic" in query:
            webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Visual Studio 6.0")
            speak("Opening visual Basic")
        elif "open whatsapp" in query:
            webbrowser.open("C:/Users/Anand swaroop/Downloads/WhatsAppSetup.exe")
            speak("opening whatsapp")
        elif "open chrome" in query:
            webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome")
            speak("Opening chrome")
        elif 'open youtube' in query:
            speak("Going Youtube...")
            webbrowser.open("youtube.com")
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'search youtube' in query:
            query = query.replace("youtube ","")
            speak("Searching for",query)    
            webbrowser.open("www.youtube.com/search?q="+query)
            speak("Searching into youtube")   
        elif 'genrate password' in query:
            alp = 'bcdefghijklmnopqrstuvwxyz'       
            num = '1234567890'
            sym = '!@#$%^&*()_+-*/.><?/}{[]'
            all = num+alp+sym
            length   = int(input(speak("what length should be")))
            passcode =  "".join(random.sample(all,length))
            speak("You may try this one")
            print(passcode)
        elif 'open code' in query:
            os.startfile("C:/Users/Anand swaroop/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code")
            speak("Opening code...")
        elif 'open' in query:
            query2 = query.replace("open ","")
            os.startfile(query2)
            speak("opening",query2,"...")
        elif 'google' in query:
            query = query.replace("google ","")
            print("Searching for",query)    
            webbrowser.open("www.google.com/search?q="+query)
            speak("Searching into google")   
        elif "add" in query:
            print("sum = ",int(input("no.1: "))+int(input("no.2: ")))
        elif "subtract" in query:
            print("Difference = ",int(input("no.1: "))-int(input("no.2: ")))       
        elif "multiply" in query:
            print("Product = ",int(input("no.1: "))*int(input("no.2: ")))           
        elif "divide" in query:
            print("Quotient = ",int(input("no.1: "))/int(input("no.2: ")))           
        elif "square" in query:
            a = int(input("Whose square are you asking for?"))
            print("Square of",a,"is",a*a)
        elif "open folder" in query:
            folder = input("Tell the name or path: ")
            dri = input("Drive name: ").lower()
            os.startfile(dri+"/"+folder)
            print("Visiting",folder," ...")
        elif 'what can you do' in query:
            speak("Here is what I can do...")
            print("1. Open folders\n2. Open applications\n3. Do wikipedia search\n4. Google search\n5. Youtube search\n6. Do mathematical operations\n7. Work as a chatbot\n8. Generate Passwords\n9.Write Python code\n10. Press any key on the keyboard")    
        elif 'read file' in query:
            file = takeCommand()
            f = open(file,'r')
            content = f.read()
            print(content)
        elif 'create' and 'python code' in query:
            code1 ="""a = int(input("enter a no"))\nb = int(input("enter an no."))\nprint("their sum is",a+b)"""
            type = takeCommand("chose any one\n1.To add two numbers\n2.To print something")
            name = takeCommand("write your file name")
            name2=name+".py"
            f=open(name2,"w")
            if type=='1':
                f.write(code1)
            elif type=="2":
                printer = takeCommand("What do you wanna print: ")
                x = "print('"
                y = "')"
                z = x+printer+y
                code2 =z
                f.write(code2)
            else:break
            f.close()
            print("File created !!")
        elif 'go to' in query:
            query = query.replace("go to","")
            x = "Going",query,"..."
            speak(x)
            webbrowser.open("www.google.com/search?q="+query)
        elif 'pause' in query:
                keyboard.press('k')
        elif 'restart' in query:
                keyboard.press("0")
        elif "mute" in query:
                keyboard.press("m")
        elif "skip" in query:
                keyboard.press("l")
        elif "back" in query:
                keyboard.press("j")
        elif "full screen" in query:
                keyboard.press("f")
        elif "exit full screen" in query:
                keyboard.press("ecsape")       
        elif "create notepad file" in query:
            speak("What should I name it? ")
            name = takeCommand()
            speak("Where should I create it? ")
            f = open(name,"w")
            speak("Create Successfully !!")
            speak("Now, what should I write on it ")
            txt = takeCommand().lower()
            if txt =="nothing":
                pass
            elif txt==txt:
                f.write(txt)
            else:pass
            speak("Done")
        elif "close everything" in query:
            keyboard.press_and_release("Alt + F4")
            keyboard.press_and_release("Alt + F4")
            keyboard.press_and_release("Alt + F4")
        elif 'save a password' in query:
            speak("What's the password")
            password = str(input(": "))
            # password = takeCommand()
            speak("Whose password is that?")
            name = str(input(": "))
            # name = takeCommand()
            f = open('Password.txt','w')
            content = name ,password
            f.write("1234") 
            speak("File created! of name Passwprd.txt")
            f.close()
        elif 'make' and 'changes' in query:
            speak("Okay sir, I am shutting down for a while")
            quit()
        elif 'reboot' in query:
            speak("As you wish sir")
            keyboard.press_and_release("Ctrl + F5")
            quit()
        elif 'write' in query:
            speak("Ok START")
            content = takeCommand()
            f = open("Information.txt",'w')
            f.write(content)
            f.close()
            speak("Saved this in Information.txt")
        elif 'good' in query:
            speak("Thanks for the complement")
        
        else:pass
