from tkinter import *
from PIL import ImageTk,Image

win = Tk()
win.title("APP")
win.geometry('650x400')
#win.iconbitmap('C:\\Users\\tanis\\OneDrive\\Desktop\\runtime')
myimg = ImageTk.PhotoImage(Image.open("lady.jpeg"))
mylabel = Label(win,image = myimg)
mylabel.grid(row = 0,column = 0,rowspan = 7)
lab1 = Label(win,text = "Welcome to RUNTIME TERROR",font = 32,bg = "green")
lab1.grid(row = 0,column = 1)
lab2 = Label(win,text = "Rules: \n 1.Start from the first level \n 2.The first few levels teaches you basics \n 3.Fifth level teaches you python basics \n 4.Click on start to start the game ",font = 20)
lab2.grid(row = 1,column = 1)
def onstart():
    import alllevels
start_btn = Button(win,text = "START",bg = "red",command = lambda : onstart())
start_btn.grid(row = 5,column = 2)
win.mainloop()
