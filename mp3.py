from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import pygame
import pickle
from PIL import ImageTk, Image
from mutagen.mp3 import MP3
import time
import random
import tkinter.ttk as ttk
import os
import youtube_dl

top=Tk()
top.title('MP3')
top.geometry('780x500')
logo=PhotoImage(file='images/mp3logo1.png')
top.iconphoto(False,logo)
top.configure(background='#DED7C9')

pygame.mixer.init()

scroll=Scrollbar(top,orient=VERTICAL)
playlist=Listbox(top,width=50,height=20,bg='#B2A893',fg='black',font='bold',selectbackground='white',selectforeground='black',yscrollcommand=scroll.set)
playlist.pack(padx=30)
scroll.config(command=playlist.yview)
scroll.place(relx = 1.0,rely = 0.0,relheight=1,anchor ='ne')


la=Label(top)
def length():
    global la
    global duration
    la.place_forget()
    lensong=True
    lensong=playlist.curselection()
    song=playlist.get(lensong)
    song=fr'C:\Users\ADMIN\Desktop\MP3 CS Project\songs\{song}.mp3'
    anasong=MP3(song)
    duration=anasong.info.length
    durationtime=time.strftime('%M:%S',time.gmtime(duration))
    la=Label(top,text=str(durationtime))
    la.config(font=('Helvetica bold',40))
    la.place(x=620,y=0)
    if lensong==False:
        la.place_forget()

   
def shuffle():
    allsongs=playlist.get(0,END)
    allsongs=list(allsongs)
    random.shuffle(allsongs)
    playlist.delete(0,END)
    for i in allsongs:
        playlist.insert(END,i)
    
def ytlink():
    global songs
    vidurl=simpledialog.askstring(title='Youtube Link',prompt='Enter Link\t\t\t')
    vid=youtube_dl.YoutubeDL().extract_info(url=vidurl,download=False)
    songs = f"{vid['title']}.mp3"
    options={'format':'bestaudio/best','keepvideo':False,'outtmpl':songs,}
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
    os.chdir('songs/')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vid['webpage_url']])
    
    

    


    
def add():
    add_song=filedialog.askopenfilename(initialdir='songs/',title='Choose a song',filetypes=(('mp3','*.mp3'),))
    
    add_song=add_song.replace("C:/Users/ADMIN/Desktop/MP3 CS Project/songs/","")
    add_song=add_song.replace('.mp3','')

    playlist.insert(END,add_song)
def addmultiple():

    add_songs=filedialog.askopenfilenames(initialdir='songs/',title='Choose a song',filetypes=(('mp3','*.mp3'),))

    for add_song in add_songs:
        add_song=add_song.replace("C:/Users/ADMIN/Desktop/MP3 CS Project/songs/","")
        add_song=add_song.replace('.mp3','')
        playlist.insert(END,add_song)

def savefile():
    savemp3=filedialog.asksaveasfilename(initialdir='saved playlists/',filetypes=(('Text Document','*.txt'),))
    playlists=playlist.get(0,END)
    playlists=list(playlists)
    file=open(savemp3,'wb')
    pickle.dump(playlists,file)
    file.close()

def openplaylists():
    openmp3=filedialog.askopenfilename(initialdir='saved playlists/',title='Choose playlist',filetypes=(('All Files','*.*'),))
    file1=open(openmp3,'rb')
    open12=pickle.load(file1)
    for i in open12:

        playlist.insert(END,i)

def remove():
    playlist.delete(0,END)
    pygame.mixer.music.stop()
    la.place_forget()

def removeone():
    playlist.delete(ANCHOR)
    pygame.mixer.music.stop()


def playsong():
    song=playlist.get(ACTIVE)
    song=fr'C:\Users\ADMIN\Desktop\MP3 CS Project\songs\{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
        


paused=False
def pausesong(pau):
    global paused
    paused=pau
    if paused==True:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

def fowardsong():
    fowsong=playlist.curselection()
    fowsong=fowsong[0]+1
    song1=playlist.get(fowsong)
    song1=fr'C:\Users\ADMIN\Desktop\MP3 CS Project\songs\{song1}.mp3'
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(loops=0)
    playlist.selection_clear(0,END)
    playlist.activate(fowsong)
    playlist.selection_set(fowsong,last=None)

def backwardsong():
    backsong=playlist.curselection()
    backsong=backsong[0]-1
    song1=playlist.get(backsong)
    song1=fr'C:\Users\ADMIN\Desktop\MP3 CS Project\songs\{song1}.mp3'
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(loops=0)
    playlist.selection_clear(0,END)
    playlist.activate(backsong)
    playlist.selection_set(backsong,last=None)



def stopmusic():
    pygame.mixer.music.stop()
    playlist.selection_clear(ACTIVE)
    la.place_forget()

def volumecont(a):
    pygame.mixer.music.set_volume(volume.get())
    curvol = pygame.mixer.music.get_volume()
    curvol = curvol * 100
    if int(curvol) < 1:
        volmeter.config(image=novolo)
    elif int(curvol)>0 and int(curvol)<=25:
        volmeter.config(image=vol1o)
    elif int(curvol)>=25 and int(curvol)<=50:
        volmeter.config(image=vol2o)
    elif int(curvol)>=50 and int(curvol)<=100:
        volmeter.config(image=vol3o)

    


menu0=Menu(top)                 #Creating menu
top.config(menu=menu0)

addsong=Menu(menu0)             #Creating add song menu
menu0.add_cascade(label='Playlist',menu=addsong)
addsong.add_command(label='Add a song',command=lambda:add())
addsong.add_command(label='Add multiple songs',command=lambda:addmultiple())

save=Menu(menu0)
menu0.add_cascade(label='Save',menu=save)
save.add_command(label='Save Playlist',command=lambda:savefile())
save.add_command(label='Open playlist',command=lambda:openplaylists())
delete=Menu(menu0)
menu0.add_cascade(label='Clear',menu=delete)
delete.add_command(label='Clear Playlist',command=lambda:remove())
delete.add_command(label='Delete Song from Playlist',command=lambda:removeone())

feat=Menu(menu0)
menu0.add_cascade(label='Features',menu=feat)
feat.add_command(label='Length of song',command=lambda:length())
feat.add_command(label='Shuffle Playlist',command=shuffle)
feat.add_command(label='Convert Youtube link to MP3',command=lambda:ytlink())

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

global novolo
global vol1o
global vol2o
global vol3o

novol=PhotoImage(file='images/no vol.png')
vol1=PhotoImage(file='images/vol 1.png')
vol2=PhotoImage(file='images/vol 2.png')
vol3=PhotoImage(file='images/vol 3.png')

novolo=novol.subsample(10,10)
vol1o=vol1.subsample(10,10)
vol2o=vol2.subsample(10,10)
vol3o=vol3.subsample(10,10)

buttonframe=Frame(top)
buttonframe.pack()
buttonframe.configure(background='#DED7C9')
background=ImageTk.PhotoImage(file='images/mp3logo12.png')
labe=Label(buttonframe,image=background,background='#DED7C9')
labe.grid(row=0,column=0)


foward_=Button(buttonframe,image=foward2image,borderwidth=0,bg='#DED7C9',activebackground='#DED7C9',command=lambda:fowardsong())
backward=Button(buttonframe,image=backward2image,borderwidth=0,bg='#DED7C9',activebackground='#DED7C9',command=lambda:backwardsong())
play=Button(buttonframe,image=play2image,borderwidth=0,bg='#DED7C9',activebackground='#DED7C9',command=lambda:playsong())
stop=Button(buttonframe,image=stop2image,borderwidth=0,bg='#DED7C9',activebackground='#DED7C9',command=lambda:stopmusic())
pause=Button(buttonframe,image=pause2image,borderwidth=0,bg='#DED7C9',activebackground='#DED7C9',command=lambda:pausesong(paused))


foward_.grid(row=0,column=7)
backward.grid(row=0,column=1)
play.grid(row=0,column=4)
pause.grid(row=0,column=2)
stop.grid(row=0,column=6)



volume=ttk.Scale(top, from_=1,to=0,orient=VERTICAL,value=1,command=volumecont,length=140)
volume.place(relheight=0.6)
volname=Label(top,text='Volume')
volname.place(y=300)
volmeter=Label(top,image=vol3o,background='#DED7C9')
volmeter.place(x=40,y=150)


mainloop()