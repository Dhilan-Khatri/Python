from tkinter import *
window=Tk()
window.geometry("400x400")
window.title("Create Account")

frame=Frame(master=window, height=200, width=360, bg="lightblue")
nameUsername=Label(frame, text="Enter Username", bg="cyan", fg="black")
nameEmail=Label(frame, text="Enter Email", bg="cyan", fg="black")
namePassword=Label(frame, text="Enter Password", bg="cyan", fg="black")

inUsername=Entry(frame)
inEmail=Entry(frame)
inpassword=Entry(frame, show="*")
def display():
    name=inUsername.get()
    greet="Hello "+name
    message="\n Thanks for creating your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
textbox=Text(bg="white", fg="black")
button=Button(text="Create Account", command=display, bg="white")
frame.place(x=20,y=0)

nameUsername.place(x=20, y=20)
inUsername.place(x=150, y=20)
nameEmail.place(x=20, y=80)
inEmail.place(x=150,y=80)
namePassword.place(x=20, y=140)
inpassword.place(x=150, y=140)
button.place(x=130, y=210)
textbox.place(y=270)

window.mainloop()