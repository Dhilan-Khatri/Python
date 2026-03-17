from tkinter import *
from tkinter import messagebox, ttk

class restuarantManagment:
    def __init__(self, root):
        self.root=root
        self.root.title("Restaurant Management System")

        self.menuItems={"Breakfast Meal":12, "Lunch Meal":12, "Dinner Meal":12, "Fries":2, "Soda":2, "Burger Meal":10 }
        self.exchangeRate=82
        self.setUpBackground(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        ttk.Label(frame, text="Restaurant Management", font=("Ariel", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)
        self.menuLabels={}
        self.menuQuantities={}
        for i, (item, price) in enumerate(self.menuItems.items(), start=1):
            label=ttk.Label(frame, text=f"{item}  (${price})", font=("Ariel", 12))
            label.grid(row=i, padx=10, pady=10)
            self.menuLabels[item]=label
            quantityEntry=ttk.Entry(frame, width=5)
            quantityEntry.grid(row=i, column=1, padx=10, pady=5)
            self.menuQuantities[item]=quantityEntry
        self.currency=StringVar()
        Label(frame, text="Currency:", font=("Ariel", 12)).grid(row=len(self.menuItems)+1, column=0, padx=10, pady=5)
        currencyDropdown=ttk.Combobox(frame, textvariable=self.currency, state="readonly", width=18, values=("USD", "INR"))
        currencyDropdown.grid(row=len(self.menuItems)+1, column=1, padx=10, pady=5)
        currencyDropdown.current(0)
        self.currency.trace("W", self.updateMenuPrices)
        orderButton=ttk.Button(frame, text="Place Order", command=self.placeOrder)
        orderButton.grid(row=len(self.menuItems)+2, columnspan=3, padx=10, pady=5)
        def setupBackground(self, root):
            canvas=Canvas(root, width=800, height=600)
            canvas.pack()
            orginalImage=PhotoImage(file="download.png")
            backgroundImage=orginalImage.subsample(orginalImage.width()//800, orginalImage.height()//600)
            canvas.create_image(0,0, anchor=ttk.NW, image=backgroundImage)
            canvas.image=backgroundImage
    window.geometry("600x600")
    window.mainloop()