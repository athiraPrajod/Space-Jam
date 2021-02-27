import sys
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *

HEIGHT = 1000
WIDTH = 1000
global total
root = tk.Tk()
root.title("Quiz")
root.configure(background = "black")
root.geometry('%dx%d' % (WIDTH,HEIGHT))

myFont = font.Font(family='Helvetica', size = 20)


q1 = Label(root, text = "Question 1", font = ("Arial", 30)).pack()
Q1 = Label(root, text = "Which of these is a keyword?", font = ("Arial", 30)).pack()

"""def click():
    if( == opts[0]):"""


#.grid(row = 0, column = 0, padx = 10, pady = 10)
def options(i, txt):
    bt = tk.Button(root, text = "%d) %s" % (i,txt), font = myFont)
    bt.pack(pady = 20)


opts = ["float", "accept", "keyword", "bool"]

for i in range(1,5):
    options(i,opts[i-1])

contImg = tk.PhotoImage(file = "Continue.png")
contBtn = tk.Button(root, image = contImg, border = 0).pack(pady = 30)


root.mainloop()