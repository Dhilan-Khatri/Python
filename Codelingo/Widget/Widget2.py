from tkinter import *
import time
window=Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")

mainLabel=Label(text="Hey There!", fg="White", bg="Black", width=400, height=1)
mainLabel.pack()
nameLabel=Label(text="Full Name", bg="White")
nameLabel.pack()
nameEntry=Entry()
nameEntry.pack()
def display():
    name=nameEntry.get()
    global message
    message="Welcome to the Application \n"
    greet="Hello " + name +"\n" 
    date= time.localtime()
    textbox.insert(END, greet)
    textbox.insert(END, message)
    textbox.insert(END, date)
textbox=Text(height=3)
button=Button(text="Begin", command=display, height=1, bg="Blue", fg="Green")
button.pack()
textbox.pack()

window.mainloop()