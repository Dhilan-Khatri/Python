from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("Interest Calculator")

principle1 = Label(window, text="Enter Principal", bg="light grey")
time1 = Label(window, text="Enter Time", bg="light grey")
rate1 = Label(window, text="Enter Rate", bg="light grey")
principle2 = Entry(window)
time2 = Entry(window)
rate2 = Entry(window)
textbox = Text(bg="white", fg="black", height=6, width=35)

def calculate():
    principal = float(principle2.get())
    time = float(time2.get())
    rate = float(rate2.get())
    simple = (principal * rate * time) / 100
    compound = principal * ((1 + rate / 100) ** time) - principal

    textbox.delete("1.0", END)
    textbox.insert(END, "Simple Interest: " + str(simple))
    textbox.insert(END, "\nCompound Interest: " + str(compound))

button = Button(text="Calculate Interest", command=calculate, bg="light grey")

principle1.place(x=20, y=30)
principle2.place(x=180, y=30)
time1.place(x=20, y=80)
time2.place(x=180, y=80)
rate1.place(x=20, y=130)
rate2.place(x=180, y=130)
button.place(x=130, y=190)
textbox.place(x=30, y=240)

window.mainloop()
