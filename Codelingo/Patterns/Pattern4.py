n=int(input("Give A number: "))
for i in range (1, n+1, 2):
    for g in range (1, i+1):
        print(g,end=" ")
    print()
for i in range (n-2, 0, -2):
    for g in range (1, i+1):
        print(g,end=" ")
    print()