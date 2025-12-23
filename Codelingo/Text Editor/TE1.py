from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
window=Tk()
window.geometry("600x500")
window.title("Text Editor")
window.rowconfigure(0,minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def openFile():
    filePath=askopenfilename(filetypes=[("textfile", "*.txt"), ("all files", "*.*")])
    if not filePath:
        return
    textEdit.delete(1.0, END)
    with open(filePath, "r") as inputFile:
        text=inputFile.read()
        textEdit.insert(END, text)
        inputFile.close()
    window.title(f"Text Editor {filePath}")
def saveFile():
    filePath=asksaveasfilename(defaultextension="txt", filetypes=[("textfile", "*.txt"), ("all files", "*.*")])
    if not filePath:
        return
    with open(filePath, "w") as outputFile:
        text=textEdit.get(1.0, END)
        outputFile.write(text)
    window.title(f"Text Editor {filePath}")
def clearFile():
    textEdit.delete("1.0", END)
def countFile():
    text=textEdit.get("1.0", END).strip()
    words=len(text.split())
    messagebox.showinfo("Word Count", words)
textEdit=Text(window)
frame=Frame(window, relief=RAISED, bd=2)
openButton=Button(frame, text="Open", command=openFile)
saveButton=Button(frame, text="Save As", command=saveFile)
clearButton=Button(frame, text="Clear", command=clearFile)
wordButton=Button(frame, text="Word Count", command=countFile)
openButton.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
saveButton.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
clearButton.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
wordButton.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
frame.grid(row=0, column=0, sticky="ns")
textEdit.grid(row=0, column=1, sticky="nsew")
window.mainloop()