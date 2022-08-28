from tkinter import*
from tkinter import messagebox
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

def logincheck():
    u=username.get()
    p=password.get()
    if u=='' or p=='':
        messagebox.showinfo('','Dont leave any fields blank')
    elif u=='ashhumkar'and p=='dingdang':
        messagebox.showinfo('','Login successful')
        root.destroy()
        open()

    else:
        messagebox.showinfo('','Unsuccessful')
    

def loginn():
    global root

    root=Tk()
    root.geometry('300x300')
    root.title('Test login')
    global username
    global password
    username=StringVar()
    password=StringVar()
    lb=Label(root,width=50,text='Enter your login details',fg='black',bg='yellow').place(x=0,y=0)
    loginlabel=Label(root,text='Username ').place(x=5,y=30)
    login=Entry(root,width=30,textvariable=username).place(x=80,y=30)
    passwordlabel=Label(root,text='Password ').place(x=5,y=50)
    password0=Entry(root,textvariable=password,width=30,show='*',).place(x=80,y=50)

    but=Button(root, text='Login',command=logincheck).place(x=10,y=80)




def open():
    top=Tk()
    top.title('MP3')
    top.geometry('780x550')
    logo=PhotoImage(file='images/mp3logo1.png')
    top.iconphoto(False,logo)
    top.configure(background='#ACAC5A')
    pygame.mixer.init()

    playlist=Listbox(top,width=50,height=20,bg='#FAFA70',fg='black',font='bold',selectbackground='white',selectforeground='black')
    playlist.pack(padx=30)

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
        la.place(relx = 1.0,rely = 0.0,anchor ='ne')
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
        global song
        vidurl=simpledialog.askstring(title='Youtube Link',prompt='Enter Link')
        vid=youtube_dl.YoutubeDL().extract_info(url=vidurl,download=False)
        song = f"{vid['title']}.mp3"
        options={'format':'bestaudio/best','keepvideo':False,'outtmpl':song,}
        os.chdir('songs/')
        with youtube_dl.YoutubeDL(options) as ydl:
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

    def slide(a):
        songs= playlist.get(ACTIVE)
        songs=fr'C:\Users\ADMIN\Desktop\MP3 CS Project\songs\{songs}.mp3'

        pygame.mixer.music.load(songs)
        pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

    def volumecont(a):
        pygame.mixer.music.set_volume(volume.get())



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


    buttonframe=Frame(top)
    buttonframe.pack()
    buttonframe.configure(background='#ACAC5A')
    background=ImageTk.PhotoImage(file='images/mp3logo12.png')
    labe=Label(buttonframe,image=background)
    labe.grid(row=0,column=0)


    foward_=Button(buttonframe,image=foward2image,borderwidth=0,bg='#ACAC5A',command=lambda:fowardsong())
    backward=Button(buttonframe,image=backward2image,borderwidth=0,bg='#ACAC5A',command=lambda:backwardsong())
    play=Button(buttonframe,image=play2image,borderwidth=0,bg='#ACAC5A',command=lambda:playsong())
    stop=Button(buttonframe,image=stop2image,borderwidth=0,bg='#ACAC5A',command=lambda:stopmusic())
    pause=Button(buttonframe,image=pause2image,borderwidth=0,bg='#ACAC5A',command=lambda:pausesong(paused))


    foward_.grid(row=0,column=7)
    backward.grid(row=0,column=1)
    play.grid(row=0,column=4)
    pause.grid(row=0,column=2)
    stop.grid(row=0,column=6)

    my_slider = ttk.Scale(top, from_=0, to=100, orient=HORIZONTAL,style='black.Horizontal.TScale',value=0, command=slide, length=400)

    my_slider.pack(pady=10)

    volume=ttk.Scale(top, from_=1,to=0,orient=VERTICAL,value=1,command=volumecont,length=125)
    volume.place(relheight=0.6)
    volname=Label(top,text='Volume')
    volname.place(y=335)
    mainloop()


loginn()
mainloop()