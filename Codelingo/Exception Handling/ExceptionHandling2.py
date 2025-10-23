try:
    num1=(input("Enter A number: "))
    num1=int(num1)
    print(num1)
    num2=(input("Enter A number: "))
    num2=int(num2)
    print(num2)
    num3=num1/num2
    print(num3)
    
    num1=(input("Enter A number: "))
    num1=int(num1)
    print(num1)
    num2=(input("Enter A number: "))
    num2=int(num2)
    print(num2)
    num3=num1/num2
    print(num3)
except ValueError as ex:
    print("Please Enter Vaild Intiger Input")
except ZeroDivisionError as ex:
    print("Number can not be divided. Please enter valid number.")
except SyntaxError as ex:
    print("Please check syntax.")
except IndentationError as ex:
    print("Code format is invaid.")
except:
    print("Wrong input.")
finally:
    print("I will always get executed.")