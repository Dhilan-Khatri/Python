from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")

input=Entry(window)
input.pack()
input2=Entry(window)
input2.pack()

def check():
    num1=int(input.get())
    num2=int(input2.get())
    if num1 > 0 and num2 > 0:
        messagebox.showinfo("Result", f"The sum is {num1+num2}")
    else:
        retry=messagebox.askretrycancel("Invaild Input", "1 or Both numbers are negative do you want to retry")
        if retry:
            input.delete(0, END)
            input2.delete(0,END)
button=Button(text="check", command=check)
button.pack()
window.mainloop()