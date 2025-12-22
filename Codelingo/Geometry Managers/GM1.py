from tkinter import * 
window=Tk()

frame1=Frame(master=window, width=100, height=100, bg="red")
frame1.pack(side=TOP)

frame2=Frame(master=window, width=50, height=50, bg="green")
frame2.pack(side=LEFT)

frame3=Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(side=LEFT)

window.mainloop()