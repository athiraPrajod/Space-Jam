from tkinter import *
#import level3
lvl_pg=Tk()
lvl_pg.geometry("500x500")
l1=Label(lvl_pg,text="Game overview",font = ('bold',24))
l1.grid(row=0, column=0 ,columnspan=3)

def call1():
    import Level1
def call2():
    import level2
def call5():
    import level3
    
level1=Button(lvl_pg, text="Level 1",padx = 20,pady = 20,command = lambda : call1())
level1.grid(row=1, column=0, padx=10,pady=5 )
level2=Button(lvl_pg, text="Level 2",padx = 20,pady = 20, command = lambda : call2() )
level2.grid(row=1, column=1, padx=10,pady=5)
level3=Button(lvl_pg, text="Level 3", state=DISABLED,padx = 20,pady = 20)
level3.grid(row=1, column=2, padx=10,pady=5)
level4=Button(lvl_pg, text="Level 4", state=DISABLED,padx = 20,pady = 20)
level4.grid(row=2, column=0, padx=10,pady=5)
level5=Button(lvl_pg, text="Level 5",padx = 20,pady = 20,command = lambda : call5())
level5.grid(row=2, column=1, padx=10,pady=5)
level6=Button(lvl_pg, text="Level 6", state=DISABLED,padx = 20,pady = 20)
level6.grid(row=2, column=2, padx=10,pady=5)
level7=Button(lvl_pg, text="Level 7", state=DISABLED,padx = 20,pady = 20)
level7.grid(row=3, column=0, padx=10,pady=5)
level8=Button(lvl_pg, text="Level 8", state=DISABLED,padx = 20,pady = 20)
level8.grid(row=3, column=1, padx=10,pady=5)
level9=Button(lvl_pg, text="Level 9", state=DISABLED,padx = 20,pady = 20)
level9.grid(row=3, column=2, padx=10,pady=5)

lvl_pg.mainloop()
