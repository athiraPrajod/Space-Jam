import sys
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *

HEIGHT = 1000
WIDTH = 1000
global total
global radiovar
root = tk.Tk()
root.title("Quiz")
root.configure(background = "black")
root.geometry('%dx%d' % (WIDTH,HEIGHT))
myFont = font.Font(family='Helvetica', size = 20)

questions = [
    "Which of these is a keyword?",
    "Is Python case sensitive when dealing with identifiers?",
    "Which of the following is an invalid variable?",
    "Which one of the following is the correct extension of the Python file?"
]

answers = [["float", "accept", "keyword", "bool"],
    ["Yes", "No", "Machine dependent", "Can't say"],
    ["my_string_1","1st_string", "foo", "_"],
    [".python",".py", ".p", "None of the above"]
]

def nextPressed():
    Q1.destroy()
    contBtn.destroy()

def selected():
    global radiovar
    x = radiovar.get()
    print(x)

def buttons(l):

    global radiovar
    radiovar = tk.IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(
        root,
        text = l[0],
        value = 0,
        variable = radiovar,
        command = selected
    )
    r1.pack(pady = 20)

    r2 = Radiobutton(
        root,
        text = l[1],
        value = 0,
        variable = radiovar,
        command = selected
    )
    r2.pack(pady = 20)

    r3 = Radiobutton(
        root,
        text = l[2],
        value = 0,
        variable = radiovar,
        command = selected
    )
    r3.pack(pady = 20)

    r4 = Radiobutton(
        root,
        text = l[3],
        value = 0,
        variable = radiovar,
        command = selected
    )
    r4.pack(pady = 20)


    """contImg = tk.PhotoImage(file = "Continue.png")
    contBtn = tk.Button(root, image = contImg, border = 0, command = nextPressed)
    contBtn.pack(pady = 30)"""

# Question 1
Q1 = Label(root, text = "Which of these is a keyword?", font = ("Arial", 30))
Q1.pack()
buttons(answers[0])

#contImg = tk.PhotoImage(file = "Continue.png")
contBtn = tk.Button(root, text = "Continue", border = 0, command = nextPressed)
contBtn.pack(pady = 30)

# Question 2
#Q2 = Label(root, text = "Is Python case sensitive when dealing with identifiers?", font = ("Arial", 30))
#Q1.pack()
#buttons(answers[1])

root.mainloop()