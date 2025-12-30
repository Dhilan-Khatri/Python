from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window=Tk()
window.geometry("650x400")
window.title("Denomination Counter")
window.configure(bg="light blue")
upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(window, image=image, bg="light blue")
label.place(x=180, y=20)
label1=Label(window, text="Hello User, Welcome to Denomination Calulator", bg="light blue")
label1.place(relx=0.5, y=360, anchor=CENTER)
def message():
    messagebox1=messagebox.showinfo("Alert", "Do you want to calulate the denomination count?")
    if messagebox1 =="ok":
        topwindow()
button=Button(window, text="Let's get started", command=message, bg="brown", fg="white")
button.place(x=260, y=360)
def topwindow():
    top=Toplevel()
    top.title("Denomination Counter")
    top.configure(bg="light grey")
    top.geometry("600x450")
    label2=Label(top, text="Enter Total Amount", bg="light grey")
    entry=Entry(top)
    label3=Label(top, text="Here are # of bills for each denomination", bg="light grey")
    l1=Label(top, text="100", bg="light grey")
    l2=Label(top, text="50", bg="light grey")
    l3=Label(top, text="20", bg="light grey")
    l4=Label(top, text="10", bg="light grey")
    l5=Label(top, text="1", bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    t4=Entry(top)
    t5=Entry(top)
    def calculator():
        try:
            global amount
            amount=int(entry.get())
            hundreds=amount//100
            amount=amount%100
            fifties=amount//50
            amount=amount%50
            twenties=amount//20
            amount=amount%20
            tens=amount//10
            amount=amount%10
            ones=amount//1
            t1.delete(0, END)
            t1.insert(0, str(hundreds))
            t2.delete(0, END)
            t2.insert(0, str(fifties))
            t3.delete(0, END)
            t3.insert(0, str(twenties))
            t4.delete(0, END)
            t4.insert(0, str(tens))
            t5.delete(0, END)
            t5.insert(0, str(ones))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    button2=Button(top, text="Calculate", command=calculator, bg="brown", fg="white")
    label2.place(x=230, y=50)
    entry.place(x=200, y=80)
    button2.place(x=240, y=120)
    label3.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)
    l5.place(x=180, y=320)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)
    t5.place(x=270, y=320)
    top.mainloop()
window.mainloop()