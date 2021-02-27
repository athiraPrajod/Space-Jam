from tkinter import *
from PIL import ImageTk, Image
from random import choice
from random import shuffle

root=Tk()
#root.geometry("600x400+-1900+100")
root.geometry("700x700")
root.title("Word Jumble")
my_img=ImageTk.PhotoImage(Image.open("pic.png"))
my_label=Label(image=my_img)
my_label.pack()
wel_lab=Label(root, text="Hello and welcome to level one of Runtime Terror!")
wel_lab.pack()
lab2=Label(root, text="In this game you need to find the correct word using the jumbled words.\nClick on 'Answer' after typing the word in the text box.\nIf you got it correct click on 'Next Word' otherwise try again \n Stuck?\nClick on Hint to get help")
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

    # List of programming terms words
    prog_terms = ['functions', 'array', 'classes', 'objects', 'API', 'variables', 'if else', 'iteration', 'comments', 'Boolean', 'Kubernetes', 'Docker' 'Cloud Computing', 'Machine Learning', 'Data types', 'Keywords', 'NULL', 'Package']
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
        top=Toplevel()
        lvl_comp_lab=Label(top,text=" Congratulations,Level Completed!")
        lvl_comp_lab.pack()
        lvl2=Button(top, text="Click here to go to Level 2")
        lvl2.pack()

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

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=10)

my_button = Button(button_frame, text="Next word", command=shuffler)
my_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)



answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

hint_label = Label(root, text='', font=("Helvetica", 18))
hint_label.pack(pady=10)

shuffler()
root.mainloop()
