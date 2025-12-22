from tkinter import *
from datetime import date

window = Tk()
window.geometry("400x400")
window.title("Age Calculator")

frame = Frame(master=window, height=400, width=400, bg="lightgrey")

nameLabel = Label(frame, text="Enter Name")
dayLabel = Label(frame, text="Enter Day #")
monthLabel = Label(frame, text="Enter Month #")
yearLabel = Label(frame, text="Enter Year #")

nameEntry = Entry(frame)
dayEntry = Entry(frame)
monthEntry = Entry(frame)
yearEntry = Entry(frame)

def display():
    name = nameEntry.get()
    day = dayEntry.get()
    month = monthEntry.get()
    year = yearEntry.get()
    day = int(day)
    month = int(month)
    year = int(year)
    today = date.today()
    birthDate = date(year, month, day)
    age = today.year - birthDate.year
    if (today.month, today.day) < (birthDate.month, birthDate.day):
        age -= 1
    textbox.delete("1.0", END)
    textbox.insert(END, "Hello " + name)
    textbox.insert(END, "\nYou are " + str(age) + " years old.")

textbox = Text(bg="white", fg="black", height=4, width=40)
button = Button(text="Calculate Age", command=display, bg="white")

frame.place(x=20, y=0)
nameLabel.place(x=20, y=20)
nameEntry.place(x=150, y=20)
dayLabel.place(x=20, y=70)
dayEntry.place(x=150, y=70)
monthLabel.place(x=20, y=120)
monthEntry.place(x=150, y=120)
yearLabel.place(x=20, y=170)
yearEntry.place(x=150, y=170)
button.place(x=140, y=250)
textbox.place(x=20, y=290)

window.mainloop()
