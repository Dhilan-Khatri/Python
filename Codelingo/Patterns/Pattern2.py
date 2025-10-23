
amt=int(input("Give A number: "))
n=1
for i in range (amt):
    for g in range (i+1):
        print(n, end=" ")
        n+=1
    print()