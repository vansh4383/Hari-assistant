import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour) #current time
    if hour>=0 and hour<=12:
        speak(" radhee krishna ji ,its  Morning already ")
    elif hour >12 and hour<=18:
        speak("radhee krishna ji ,its Afternoon have you ate your parsaadamm ")

    else:
        speak("radhee krishna ji, its Evening ready for aarti ")

    speak("Please tell me, How can I serve you ?")