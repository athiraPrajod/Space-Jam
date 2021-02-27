from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("APP")
root.geometry('450x400')
root.config(bg = "yellow")
#root.iconbitmap('C:\\Users\\tanis\\OneDrive\\Desktop\\runtime')
myimg = ImageTk.PhotoImage(Image.open("password.png"))
mylabel = Label(root,image = myimg)
mylabel.grid(row = 0,column = 0)
lab1 = Label(root,text = "Please help me unlock my PC",font = 24)
lab1.grid(row = 1,column = 0)
lab2 = Label(root,text = "It is a 5 digit password. Solve the following questions to get the password")
lab2.grid(row = 2,column = 0)
lt = [mylabel,lab1,lab2]

def nxt_page(btn_nxt,lt,i):
    clear(btn_nxt,lt)
    new_pg(i)

def clear(btn_nxt,lt):
    for i in lt:
        i.destroy()
    btn_nxt.destroy()

def new_pg(i):
    main = Tk()
    main.title("APP")
    if i == 1:
            i = i + 1
            ques1 = Label(main,text = "1. Find no. of syntax errors in the following code",font = 20)
            ques1.grid(row = 0,column = 0,columnspan = 4)
            ques1_1 = Label(main,text = "print(Hello world) \n x = 10 \n y = 20 \n print(x,y,sep == \"/t\") \n if x > y \n \t print(\"Greater no. is\",x) \n else: \n print(\"Greater no. is\",y)")
            ques1_1.grid(row = 1,column = 0)
            ans1 = Entry(main,width = 10)
            ans1.grid(row = 2,column = 0)
            lt = [ques1,ques1_1,ans1]
            btn_nxt = Button(main,text = "NEXT",bg = "red",command = lambda : nxt_page(btn_nxt,lt,i))
            btn_nxt.grid(row = 3,column = 1)
    elif i == 2:
            i = i + 1
            ques2 = Label(main,text = "2. What will be the output of the following code?",font = 20)
            ques2.grid(row = 0,column = 0,columnspan = 4)
            ques2_2 = Label(main,text = "list1 = [0,2,100,54,5,32,75,10,15,23,7] \n list1.sort() \n list1.reverse() \n print(list1[-2])")
            ques2_2.grid(row = 1,column = 0)
            ans2 = Entry(main,width = 10)
            ans2.grid(row = 2,column = 0)
            lt = [ques2,ques2_2,ans2]
            btn_nxt = Button(main,text = "NEXT",bg = "red",command = lambda : nxt_page(btn_nxt,lt,i))
            btn_nxt.grid(row = 3,column = 1)
    elif i == 3:
            i = i + 1
            ques3 = Label(main,text = "3. What will be the output of the following code?",font = 20)
            ques3.grid(row = 0,column = 0,columnspan = 4)
            ques3_3 = Label(main,text = "def func(x): \n func1(): \n print(x^15) \n func1() \n func(8)")
            ques3_3.grid(row = 1,column = 0)
            ans3 = Entry(main,width = 10)
            ans3.grid(row = 2,column = 0)
            lt = [ques3,ques3_3,ans3]
            btn_nxt = Button(main,text = "NEXT",bg = "red",command = lambda : nxt_page(btn_nxt,lt,i))
            btn_nxt.grid(row = 3,column = 1)
    elif i == 4:
            i = i + 1
            ques4 = Label(main,text = "4. State True(1) or False(0)",font = 20)
            ques4.grid(row = 0,column = 0,columnspan = 4)
            ques4_4 = Label(main,text = "def fn(): \n count = 1 \n def fn2(): \n global count \n count += 5 \n fn2() \n count = 0 \n fn() \n print(count) \n OUTPUT is 6")
            ques4_4.grid(row = 1,column = 0)
            ans4 = Entry(main,width = 10)
            ans4.grid(row = 2,column = 0)
            lt = [ques4,ques4_4,ans4]
            btn_nxt = Button(main,text = "NEXT",bg = "red",command = lambda : nxt_page(btn_nxt,lt,i))
            btn_nxt.grid(row = 3,column = 1)
    else:
##            mimg = ImageTk.PhotoImage(Image.open("password.PNG"))
##            mlabel = Label(main,image = mimg)
##            mlabel.grid(row = 0,column = 0)
            final = Entry(main,width = 25)
            final.grid(row = 0,column = 0)
            x = final.get()
            #x = int(y)
            def onclick(x):
                #x = final.get()
                if final.get() == "4270":
                    final_lab = Label(main,text = "CONGRATS!!! You have completed the level successfully")
                    final_lab.grid(row = 2,column = 0)
                    btn.destroy()
                else:
                    final_lab = Label(main,text = "OOPS!!Retry the level again")
                    final_lab.grid(row = 2,column = 0)
                    btn.destroy()
                btn_nxt = Button(main,text = "CLOSE")#,bg = "blue")
                btn_nxt.grid(row = 4,column = 1)
        
            btn = Button(main,text = "ENTER",command = lambda : onclick(x))
            btn.grid(row = 3,column = 0)
            #btn.destroy()
        
    
btn_nxt = Button(root,text = "NEXT",bg = "red",command = lambda : nxt_page(btn_nxt,lt,1))
btn_nxt.grid(row = 3,column = 1)

            
root.mainloop()
