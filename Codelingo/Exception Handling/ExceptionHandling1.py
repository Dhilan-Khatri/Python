try:
    num=(input("Enter A number: "))
    num=int(num)
    print(num)
except ValueError as ex:
    print("Please Enter Vaild Intiger Input")