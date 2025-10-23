import math
def Find(start, end):
    lower = math.ceil(math.sqrt(start))
    upper = math.floor(math.sqrt(end))

    if lower > upper:
        print("No square numbers in between.")
        return

    squares = [i**2 for i in range(lower, upper + 1) if start < i**2 < end]

    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print("Even square numbers between:", even_squares)
    print("Odd square numbers between:", odd_squares)

num1=int(input("Please Enter Starting Number: "))
num2=int(input("Please Enter Ending Number: "))
print(Find(num1, num2))