from tkinter import * 
window=Tk()
window.geometry("400x400")
window.title("Length Converter App")

nameLabel=Label(text="Enter Lenght in Inches", bg="lightgrey")
nameLabel.pack()
nameEntry1=Entry()
nameEntry1.pack()

def convert():
    num1=nameEntry1.get()
    num2=int(num1)*2.54
    textbox.insert(END, num1)
    textbox.insert(END," Inches = ")
    textbox.insert(END, num2)
    textbox.insert(END, " Centimeters")
    textbox.insert(END, "\n")
def delete():
    nameEntry1.delete(0,END)
buttonAdd=Button(text="Convert to Centimeters", bg="lightgrey", command=convert)
buttonAdd.pack()
textbox=Text(height=5)
textbox.pack()
buttonDelete=Button(text="Clear Textbox", bg="lightgrey", command=delete)
buttonDelete.pack()
window.mainloop()