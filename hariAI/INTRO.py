from tkinter import * 
from PIL import Image,ImageTk,ImageSequence
import time
import pygame  
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("E:\hariAI\AdobeStock_571818551_Preview.jpeg")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("E:\hariAI\Radha Krishna Instrumental Ringtone Flute - PagalRingtone.Com.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(20)
    root.destroy()

play_gif()
root.mainloop()
