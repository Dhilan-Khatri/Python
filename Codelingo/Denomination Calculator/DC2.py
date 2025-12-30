from tkinter import *
window=Tk()
window.geometry("400x400")
window.title("Password Strength Checker")

label=Label(window, text="Enter your password", bg="light grey")
label.pack()
entry=Entry(window)
entry.pack()

def check():
    password=str(entry.get())
    if len(password) <= 5:
        strenght1=Label(window, text="Weak", bg="red")
        strenght1.pack()
    elif 6 < len(password) < 8:
        strenght1=Label(window, text="Medium", bg="yellow")
        strenght1.pack() 
    elif 8 < len(password) < 12:
        strenght1=Label(window, text="Strong", bg="light green")
        strenght1.pack() 
    elif len(password) > 12:
        strenght1=Label(window, text="Very Strong", bg="dark green")
        strenght1.pack()
button=Button(window, text="Check", command=check, bg="light grey")
button.pack()

window.mainloop()