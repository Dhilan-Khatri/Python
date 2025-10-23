def plus(num1, num2):
    num3 = num1 + num2
    return num3
def minus(num1, num2):
    num3 = num1 - num2
    return num3
def muti(num1, num2):
    num3 = num1 * num2
    return num3
def divi(num1, num2):
    num3 = num1 / num2
    return num3
x=True

while x: 
    print("Enter Your Choice")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Mutiplication")   
    print ("4) Division")

    choice=int(input("Enter Choice 1-4: "))
    if choice > 0 and choice < 5:
        num1=int(input("Enter Number 1: "))
        num2=int(input("Enter Number 2: "))

        if choice == 1:
            result=plus(num1, num2)
            print(f"The Sum of {num1} and {num2} is {result}.")
        elif choice == 2:
            result=minus(num1, num2)
            print(f"The Remainder of {num1} and {num2} is {result}.")
        elif choice == 3:
            result=muti(num1, num2)
            print(f"The result of {num1} and {num2} is {result}.")
        elif choice == 4:
            result=divi(num1, num2)
            print(f"The divident of {num1} and {num2} is {result}.")
    else:
        print("Number is not allowed.")
    option= input("Do you want to continue y/n")
    if option == "n":
        x=False
    elif option == "y":
        x=True
    else: 
        print("Exiting Program...")
        exit