from tkinter import*
from tkinter import messagebox


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
    top.geometry('500x600')


loginn()
mainloop()