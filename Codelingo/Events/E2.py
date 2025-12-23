from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("300x300")

def message():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button=Button(text="Scan for Virus", command=message)
button.pack()
window.mainloop()