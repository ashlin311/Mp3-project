
from socket import SO_LINGER
from tkinter import *
from tkinter import filedialog
import pygame

top=Tk()
top.title('MP3')
top.geometry('700x500')

pygame.mixer.init()

playlist=Listbox(top,width=20,height=20,bg='#F7F494',fg='black',font='bold',selectbackground='white',selectforeground='black')
playlist.pack(padx=30)

def add():
    
    add_song=filedialog.askopenfilename(initialdir='songs/',title='Choose a song',filetypes=(('mp3','*.mp3'),))
    add_song=add_song.replace("C:/Users/ADMIN/Desktop/MP3 CS Project/songs/","")
    add_song=add_song.replace('.mp3','')

    playlist.insert(END,add_song)
    


def playsong():
    
    song=playlist.get(ACTIVE)
    song=fr'C:\Users\ADMIN\Desktop\MP3 CS Project\songs\{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
def pausesong():
    pygame.mixer.music.pause()

def stopmusic():
    pygame.mixer.music.stop()
    playlist.selection_clear(ACTIVE)

    
menu0=Menu(top)                 #Creating menu
top.config(menu=menu0)

addsong=Menu(menu0)             #Creating add song menu
menu0.add_cascade(label='Playlist',menu=addsong)
addsong.add_command(label='Add a song',command=lambda:add())


playimage=PhotoImage(file='images/play.png')
stopimage=PhotoImage(file='images/STop.png')
fowardimage=PhotoImage(file='images/foward.png')
backwardimage=PhotoImage(file='images/backward.png')
pauseimage=PhotoImage(file='images/pause.png')

play2image = playimage.subsample(4, 4)
stop2image=stopimage.subsample(6, 5)
foward2image=fowardimage.subsample(10, 10)
backward2image=backwardimage.subsample(10, 10)
pause2image=pauseimage.subsample(5,5)


buttonframe=Frame(top)
buttonframe.pack()



foward_=Button(buttonframe,image=foward2image,borderwidth=0)
backward=Button(buttonframe,image=backward2image,borderwidth=0)
play=Button(buttonframe,image=play2image,borderwidth=0,command=lambda:playsong())
stop=Button(buttonframe,image=stop2image,borderwidth=0,command=lambda:stopmusic())
pause=Button(buttonframe,image=pause2image,borderwidth=0,command=lambda:pausesong())


foward_.grid(row=0,column=6)
backward.grid(row=0,column=0)
play.grid(row=0,column=3)
pause.grid(row=0,column=1)
stop.grid(row=0,column=5)


mainloop()