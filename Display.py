from tkinter import *
from Action import Actions


def ToDisplay():
    root = Tk()
    root.title("All Contact's")
    root.geometry("400x400")
    control = Actions()
    Label(root,text=f'{control.displayall()}',width=30,font=('Times',16)).place(relx=0.4,x=20,y=20,anchor=N)
    root.mainloop()