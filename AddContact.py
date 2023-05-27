from tkinter import *
from Action import Actions

def AddToContact():
    control = Actions()
    try:
        control.add_contact(contactName.get(),contactNumber.get())
        contactName.set('')
        contactNumber.set('')
    except Exception:
        Label(root,text="Contact Already Exsists",height=4).place(relx=0.3,x=10,y=180,anchor=N)

def ToAdd():
    global root
    root = Tk()
    root.title('New Contact')
    root.geometry("400x400")
    global contactName,contactNumber
    contactName= StringVar()
    contactNumber = StringVar()
    Label(root,text='Full Name',height=4,width=10).place(relx=0.1,x=10,y=10,anchor=N)
    Entry(root,textvariable = contactName,width=50).place(relx=0.43,y=60,anchor=N)
    Label(root,text='Enter Number').place(relx=0.12,x=10,y=85,anchor=N)
    Entry(root,textvariable = contactNumber,width=50).place(relx=0.43,y=110,anchor=N)
    Button(root,text='Submit',padx=10,pady=10,command=AddToContact).place(relx=0.6,x=10,y=140,anchor=NW)
    root.mainloop()