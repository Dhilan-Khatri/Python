#age input
#if less than 0
#raise age, can not be negative
#if age is even print even 
#if age is odd print odd
try:
    age=int(input("Enter A age: "))
    if age < 0:
        raise ValueError ("Age can't be negative.")
    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd.")
except ValueError as ex:
    print(f"Invaid Age Entered {ex}")