import pyttsx3 # pyttsx3 library
import speech_recognition as rec # Speech Recognition library
import datetime # datetime library
import calendar # calendar library
import wikipedia as wiki # wikipedia library
import webbrowser as wb # web browser library
import psutil # psutil library
import pyjokes # pyjokes library
import os
import json
import requests
import wolframalpha
from threading import Thread
from urllib.request import urlopen
import random
import tkinter
from PIL import Image, ImageTk, ImageSequence
import time
import pyautogui # pyautogui library
#from uii_2 import *

root = tkinter.Tk()
engine = pyttsx3.init()
wolframalpha_app_id = 'VELJY4-6T9AT7ERX3'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Rettime():
    Time=datetime.datetime.now().strftime("%I:%M") # HH:MM 12hours format
    speak("the time is")
    speak(Time)

def Retdate():
    year = datetime.datetime.now().year
    month = calendar.month_name[datetime.datetime.now().month]
    day = datetime.datetime.now().day
    speak("The Date is")
    speak(day)
    speak(month)
    speak(year)

def cpu():
    cpu_usage = str(psutil.cpu_percent())
    speak('CPU usage is at'+cpu_usage+'percent')

def joke():
    speak(pyjokes.get_joke())

def scoon():
    image = pyautogui.screenshot()
    speak('give me the screenshot name to save it')
    imageName = HearMe()
    image.save('E:/projects/MyFirstAI/screenshots/'+imageName+'.png')
    speak('done')

def Welc():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Youssef!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Youssef!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Youssef!")
    else:
        speak("Good night Youssef!")
    #Rettime()
    #Retdate()
    #Task Greetz
    speak("TLG assistant is always awake. How can i help you?")

def hearn():
    parent = root
    canvas = tkinter.Canvas(parent, width=400, height=400)
    parent.resizable(width=False, height=False)
    #self.window = tkinter.Toplevel(self.canvas)
    canvas.pack()
    sequence = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                                Image.open(
                                r'hearn.gif'))]
    image = canvas.create_image(200,200, image=sequence[0])
    animate(1)
    parent.resizable(False, False)
    parent._offsetx = 0
    parent._offsety = 0
    parent.bind('<Button-1>',clickwin)
    parent.bind('<B1-Motion>',dragwin)
    parent.update_idletasks()
    parent.overrideredirect(1)
    parent.mainloop()

def animate(parent, counter):
    parent.canvas.itemconfig(parent.image, image=parent.sequence[counter])
    parent.parent.after(20, lambda: parent.animate((counter+1) % len(parent.sequence)))

def dragwin(self,event):
    x = self.parent.winfo_pointerx() - self.parent._offsetx
    y = self.parent.winfo_pointery() - self.parent._offsety
    self.parent.geometry('+{x}+{y}'.format(x=x,y=y))

def clickwin(self,event):
    self.parent._offsetx = event.x
    self.parent._offsety = event.y

def HearMe():
    r=rec.Recognizer()
    with rec.Microphone() as source:
        print("I'm hearing you...")
        #waitgif()
        app = Thread(target=hearn)
        app.start()
        #root.mainloop()
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Guessing what you said...")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Didn't hear anything, Say that again please.")
        return "None"
    return query

if __name__ == "__main__":

    Welc()

    while True:
        query = HearMe().lower()

        # All voice cmds will be stored as lower case string
        #for easy recognition azbi

        if 'time' in query:
            Rettime()
        
        elif 'date' in query:
            Retdate()

        elif 'n wikipedia' in query:
            speak("what should i search?")
            srch = HearMe()
            result = wiki.summary(srch,sentences=3)
            speak('According to Wikipedia.')
            print(result)
            speak(result)
        
        elif 'youtube' in query:
            speak('what you want me to search?')
            srch = HearMe().lower()
            #chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
            speak('Opening Youtube')
            wb.open('https://www.youtube.com/results?search_query='+srch)

        elif 'google' in query:
            speak('what you want me to search?')
            srch = HearMe().lower()
            speak('Opening Google')
            wb.open('https://www.google.com/search?q='+srch)

        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        
        elif 'shut down' in query:
            speak('shuting down!')
            quit()
        
        elif 'go off' in query:
            speak('going off!')
            quit()

        elif 'exit' in query:
            speak('exiting!')
            quit()

        elif 'open' in query:
            query = query.replace('open','')
            speak('opening'+query)
            if 'counter' in query:
                wb.open('steam://rungameid/10')
            if 'csgo' in query:
                wb.open('steam://rungameid/730')
        
        elif 'write' in query:
            if 'note' in query:
                speak('what you want me to write?')
                thenote = HearMe()
                file = open('notes.txt', 'w')
                speak('should i include date and time?')
                answer = HearMe()
                if 'yes' in answer or 'sure' in answer or 'of course' in answer or 'why not' in answer:
                    timestr = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(timestr)
                    file.write(':-')
                    file.write(thenote)
                    speak('your note is taken, Youssef')
                else:
                    file.write(thenote)
                    speak('okey, your note is taken')
        
        elif 'show' in query or 'read' in query:
            if 'note' in query:
                speak('Loading notes')
                file = open('notes.txt', 'r')
                notee = str(file.read())
                print(notee)
                speak(notee)
        elif 'screenshot' in query:
            scoon()
        elif 'music' in query or 'song' in query:
            songsdir = 'E:/misc'
            song = os.listdir(songsdir)
            speak('What should i play')
            selsong = HearMe().lower()
            while('number' not in selsong and 'random' not in selsong and 'you choose' not in selsong):
                speak('I could not understand, please try again')
                selsong = HearMe().lower()
            if 'number' in selsong:
                Num = int(selsong.replace('number',''))
            elif 'random' or 'you choose' in selsong:
                Num = random.randint(1,15)
            os.startfile(os.path.join(songsdir, song[Num]))
        elif 'you remember' in query:
            remember = open("remember.txt","r")
            speak('i remember that'+remember.read())
        elif 'remember' in query:
            speak('what should I remember?')
            rem = HearMe()
            speak('you asked me to remember')
            speak(rem)
            remember = open("remember.txt","w")
            remember.write(rem)
            remember.close()
        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0474ec1e5e8d45d3bf5e7ea657ccfcc1")
                data = json.load(jsonObj)
                i = 1
                speak('here are some hot news')
                print(" ******* HOT NEWS ********")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1
            except Exception as Err:
                print(str(Err))
        elif 'where is' in query:
            query = query.replace('where is','')
            speak('i will search and open Google Maps For you')
            wb.open_new_tab("https://www.google.com/maps/place/"+query)
        elif 'calculate' in query:
            ClientID = wolframalpha.Client(wolframalpha_app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            result = ClientID.query(''.join(query))
            answer = next(result.results).text
            print('Answer is : '+answer)
            speak('The answer is '+answer)
        elif 'explain' in query:
            ClientID = wolframalpha.Client(wolframalpha_app_id)
            res = ClientID.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("Nothing found")
                speak("Nothing found")
        elif 'sleep' in query:
            speak('How many seconds you want me to sleep')
            ans = int(HearMe())
            time.sleep(ans)
            speak("i'm back")
        elif 'how are you' in query:
            ans = ['i\'m fine man, no complains', 'i\'m good xD', 'today seems good i hope you the same for you', 'since you\'re here everything is good']
            speak(ans[random.randint(0, len(ans)-1)])
        
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'reboot' in query:
            os.system("shutdown /r /t 1")
        elif 'shut the system down' in query:
            os.system("shutdown /r /t 1")
            