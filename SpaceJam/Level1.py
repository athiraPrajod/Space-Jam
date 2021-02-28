from tkinter import *
from PIL import ImageTk, Image
from random import choice
from random import shuffle

root=Tk()
#root.geometry("600x400+-1900+100")
root.geometry("700x700")
root.title("Word Jumble")
##my_img=ImageTk.PhotoImage(Image.open("pic.png"))
##my_label=Label(image=my_img)
##my_label.pack()
wel_lab=Label(root, text="Hello and welcome to level one of Runtime Terror!")
wel_lab.pack()
lab2=Label(root, text="In this game you need to find the correct word using the jumbled words.\nClick on 'Answer' after typing the word in the text box.\nIf you got it correct click on 'Next Word' otherwise try again \n Stuck??\nClick on Hint to get help\nDon't know the meaning of this word?\nCLick on 'Defination' to find out!")
lab2.pack()
my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)
i=-1
def shuffler():
    global i
    i+=1
    # Clear Hint Label 
    hint_label.config(text='')

    # Clear Hint Count
    global hint_count
    hint_count = 0

    # Clear Answer Box
    entry_answer.delete(0, END)

    # Clear Answer Label
    answer_label.config(text='')

    #Clearing Defination Label
    lb.config(text='')

    # List of programming terms words
    prog_terms = ['functions', 'array', 'classes', 'objects', 'variables', 'iteration', 'comments', 'Boolean', 'Kubernetes', 'Docker'
                  , 'Machine Learning', 'Data Structures', 'Package']
    if i<len(prog_terms):
    # choosing word
        global word
        word=prog_terms[i]
        

        # Break apart our chosen word
        break_apart_word = list(word)
        shuffle(break_apart_word)
                
        # Turn shuffeled List into a word
        global shuffled_word
        shuffled_word =  ''
        for letter in break_apart_word:
            shuffled_word += letter
                
        # print shuffled word to the screen
        my_label.config(text=shuffled_word)
    else:
        lvl_comp_lab=Label(root,text=" Congratulations,Level Completed!")
        lvl_comp_lab.pack()
        bt=Button(root,text="quit" ,command=root.quit)
        bt.pack
       # def back():
        #    import alllevels
       # lvl2=Button(top, text="Close",bg = 'blue',command = lambda : back())
        #lvl2.pack()

#Creating a function to display definations        
def defination():
    d=["A function is a subprogram that acts on data and often returns a value.A function contains-\n1)function header or defination\n2)body\n3)return statement.",
       "An array is a data structure consisting of a collection of elements.",
       " A class describes the contents of the objects that belong to it:\n it describes an aggregate of data fields (called instance variables),\nand defines the operations (called methods).",
       " An object is an element (or instance) of a class; objects have the behaviors of their class.",
       "Variables are data values that can change when the user is asked a question, for example, their age.\nVariables may change during program execution. \nA variable is a memory location .\nIt has a name that is associated with that location.\nThe memory location is used to hold data.",
       "Iteration in programming means repeating steps, or instructions , over and over again.\nThis is often called a 'loop'.\nAlgorithms consist of instructions that are carried out (performed) one after another. ... Iteration is the process of repeating steps.\nThere are two ways in which programs can iterate or 'loop'count-\n1)controlled loops.\n2)condition-controlled loops.",
       "A comment is a programmer-readable explanation or annotation in the source code of a computer program.",
       "Boolean, or boolean logic, is a subset of algebra used for creating true/false statements. Boolean expressions use the operators AND, OR, XOR, and NOT to compare values and return a true or false result.",
       "Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation.\nIt has a large, rapidly growing ecosystem.\n Kubernetes services, support, and tools are widely available.\nThe name Kubernetes originates from Greek, meaning helmsman or pilot.",
       "Docker is a platform and tool for building, distributing, and running Docker containers.\nKubernetes is a container orchestration system for Docker containers that is more \nextensive than Docker Swarm and is meant to coordinate clusters of nodes at scale in production in an efficient manner.",
        "Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn\n and improve from experience without being explicitly programmed. \nMachine learning focuses on the development of computer programs that can access data\n and use it to learn for themselves.",
       "In computer science and computer programming, a data type or simply type is an attribute of data which tells the compiler or interpreter how the \nprogrammer intends to use the data.\nA data type constrains the values that an expression, such as a variable or a function, might take.",
       "Data structures are used to organize and store the data so that they can be accessed efficiently.Various python data structures are:\n1)Integers (int)\n2)Float\n3)Bollean\n4)Strings",
       "A package is basically a directory with Python files and a file with the name __init__ . \nThis means that every directory inside of the Python \npath, which contains a file named __init__ . py, will be treated as a package by Python.\n It's possible to put several modules into a Package."]

    global i
    sentence=d[i]
    lb.config(text=sentence)   
       
#Create answer Function
def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct!!")
    else:
        answer_label.config(text="Incorrect!!")

# Create Hint Counter
global hint_count
hint_count = 0

# Create Hint Function
def hint(count):
    global hint_count
    hint_count = count

    # Get the length of the chosen word
    word_length = len(word)

    # Show Hint
    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count +=1 

entry_answer = Entry(root, font=("Helvetica", 24))
entry_answer.pack(pady=20)


button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer, bg="blue",fg="white")
answer_button.grid(row=0, column=0, padx=10)

my_button = Button(button_frame, text="Next word", command=shuffler, bg="blue",fg="white")
my_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count), bg="blue",fg="white")
hint_button.grid(row=0, column=2, padx=10)

def_btn = Button(button_frame, text="Defination", command=defination, bg="blue",fg="white")
def_btn.grid(row=0, column=3, padx=10)

answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

hint_label = Label(root, text='', font=("Helvetica", 18))
hint_label.pack(pady=10)

lb = Label(root, text='')
lb.pack(pady=0)

shuffler()
root.mainloop()
