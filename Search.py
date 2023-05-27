from tkinter import *
from Action import Actions

def Seach():
    try:
        control = Actions()
        Details = control.searchContact(contactName.get())
        contactName.set('')
        Label(root,text=f'{Details}',height=4,width=30,font=('Times',12)).place(relx=0.3,x=10,y=180,anchor=N)
    except Exception:
        contactName.set('')
        Label(root,text='Contact Does Not Exsist',height=4,font=('Times',12)).place(relx=0.3,x=10,y=180,anchor=N)

def ToSeach():
    global root
    root = Tk()
    root.title("Seach Contact's Details")
    root.geometry("400x400")
    global contactName
    contactName= StringVar()
    Label(root,text='Full Name',height=4,width=10).place(relx=0.1,x=10,y=10,anchor=N)
    Entry(root,textvariable = contactName,width=50).place(relx=0.43,y=60,anchor=N)
    Button(root,text='Submit',padx=10,pady=10,command=Seach).place(relx=0.1,x=10,y=130,anchor=N)
    root.mainloop()
