row=int(input("Give A number of rows: "))
for i in range (1, row+1):
    print("*" *i)
print("\n")
for i in range (1, row+1):
    space = row - i
    star = i
    print(" " * space + "*" * star)