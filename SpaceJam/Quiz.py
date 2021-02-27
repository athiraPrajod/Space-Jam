# the json module to work with json files 
import json
import tkinter
from tkinter import *
import random


questions = [
     "Which of these is a keyword?",
     "Is Python case sensitive when dealing with identifiers?",
     "Which of the following is an invalid variable?",
     "Which of The Following is must to Execute a Python Code ?",
     "Which one of the following is the correct extension of the Python file?",
     "The append Method adds value to the list at the  ?",
     "Which one of these is floor division?",
     "Which of The following is executed in browser(client side) ?",
     "Which of the following keyword is used to create a function in Python ?",
     "To Declare a Global variable in python we use the keyword ?",
]

answers_choice = [
     ["float", "accept", "keyword", "bool"],
     ["Yes", "No", "Machine dependent", "Can't say"],
     ["my_string_1","1st_string", "foo", "_"],
     ["TURBO C","Py Interpreter","Notepad","IDE",],
     [".python",".py", ".p", "None of the above"],
     ["custom location","end","center","beginning",],
     ["/","//","%","None of the above",],
     ["perl","css","python","java",],
     ["function","void","fun","def",],
     ["all","var","let","global",],
] 


answers = [0,0,1,1,1,1,1,1,3,3] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        labelresulttext.configure(text="You have scored %d out of 25" %(score))
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= 10 and score < 20):
        labelresulttext.configure(text="You have scored %d out of 25" %(score))
        labelresulttext.configure(text="You Can Be Better !!")
    else:
        labelresulttext.configure(text="You have scored %d out of 25" %(score))
        labelresulttext.configure(text="You Should Work Hard !!")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labeltext.destroy()
    lblInstruction.destroy()
    #lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(background="black")
root.resizable(0,0)


labeltext = Label(
    root,
    text = "Quiz",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

#img2 = PhotoImage(file="Frame.png")

btnStart = Button(root, text = "Start", font = ("Arial",28,"bold"), relief = FLAT, border = 0, command = startIspressed)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Click Start when you're ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

root.mainloop()