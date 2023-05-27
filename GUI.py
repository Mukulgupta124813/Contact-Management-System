from AddContact import *
from tkinter import *
from Delete import *
from Update import *
from Display import *
from Search import *

mainWindow = Tk()
mainWindow.geometry("1000x600")
mainWindow.title('Contact Management System')
Button(mainWindow,text='Add Contact',padx=50,pady=50,bg='#26ff00',command=ToAdd).place(x=80,y=60,anchor=NW)
Button(mainWindow,text='Update Contact',padx=50,pady=50,bg='#26ff00',command=ToUpdate).place(x=350,y=60,anchor=NW)
Button(mainWindow,text='Delete Contact',padx=50,pady=50,bg='#26ff00',command=Todelete).place(x=700,y=60,anchor=NW)
Button(mainWindow,text='Display',padx=50,pady=50,bg='#26ff00',command=ToDisplay).place(x=210,y=200,anchor=NW)
Button(mainWindow,text='Search',padx=50,pady=50,bg='#26ff00',command=ToSeach).place(x=550,y=200,anchor=NW)
mainWindow.mainloop()
