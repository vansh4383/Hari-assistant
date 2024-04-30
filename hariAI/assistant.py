import pyttsx3   #module for selecting the voice 
import speech_recognition #for speech recognition
import requests    #for getting urls
from bs4 import BeautifulSoup     #beautiful soup 
import datetime      # for cuurent date and time 
import os            # for using os commands like appending files in focus mode
import pyautogui     # to use the gui in opening apps 
import webbrowser    #to open browser and all
import random        #opting the random choice
from plyer import notification    #for providing notifications 
from pygame import mixer  #for play and pause of music
import speedtest    #for wifi speed test 

for i in range(3):
    a = input("Enter Password to open hari :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [HARE KRISHNA HARI ] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
from INTRO import play_gif
play_gif

engine = pyttsx3.init("sapi5") #module 
voices = engine.getProperty("voices")  # to get the voices 
engine.setProperty("voice", voices[0].id)  # setting the voice
# print(voices[0]) #to check the type of voices
rate = engine.setProperty("rate",170)   #speaking speed of the assistant

def speak(audio):
    engine.say(audio)
    engine.runAndWait() # wait time 


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1   #listening time 
        r.energy_threshold = 300   #listening energy 
        audio = r.listen(source,0,4) #waiting time

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hare krishna " in query :
            from Greetme import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "take rest now" in query:
                    speak("thank you , You can call krishna  anytime you need him ")
                    break 


                elif "hello" in query:
                    speak(" jai shree krishna ")


                elif "aur kaise chal rha hai " in query:
                    speak("bas saab krishna ki daaya hai ")


                elif "aap kaise hoo ?" in query:
                    speak("main theek huun ,aap btao")


                elif "thank you" in query:
                    speak("you are welcome")



                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("E:\hariAI\FocusMode.py")                        
                    else:
                        pass
                
                  
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("hari","")
                    query = query.replace("translate","")
                    translategl(query)
                    
 
                elif "open" in query:             #directly search into windowsearch and enter
                    query = query.replace("open","")
                    query = query.replace("hari","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")



                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")


                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)


                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")



                elif "set an alarm" in query:
                    print("input time example:- 1 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                    exit()


                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )


                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)


                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)


                elif "wikipedia" in query:
                        from searchnow import searchWikipedia
                        searchWikipedia(query)


                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")



                elif "temperature" in query:
                    search = "temperature in mohali"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")


                elif "weather" in query:
                    search = "weather in mohali"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)               #for getting the url
                    data = BeautifulSoup(r.text,"html.parser")    #beautify the output
                    weath = data.find("div", class_ = "BNeawe s3v9rd AP7Wnd").text 
                    speak(f"current{search} is {weath}")  #tells the result


                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("hari","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()


                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")


                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    # pyautogui.sleep(1)
                    speak("SMILE")
                    pyautogui.press("enter")
                

                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())


                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=saCaYLaYyPg")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=dx4Teh-nv3A")
                    else:
                        webbrowser.open("https://www.youtube.com/watch?v=Njyx5ZuwEHI")


                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")


                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")


                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")


                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()


                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()


                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()


                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()


                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break



                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("hari","")
                    Calc(query )  

                    
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")


                elif " set my schedule" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close



                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("E:\hariAI\knock_knock.mp3")
                    mixer.music.play()
                    notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                    )
                        
                elif "go to sleep " in query:
                    speak("Going to sleep,sir")
                    exit()