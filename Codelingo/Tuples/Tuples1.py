numbertuple=(1, 2, 3, 4, 5, 6)
print(numbertuple)

fruittuple=("apple", "banana", "pear", "mango")
print(fruittuple)

print(len(fruittuple))
for i in fruittuple:
    print(i)
print(fruittuple[1:3])
#fruittuple[1]="kiwi"
#print(fruittuple)
combinetuple=fruittuple+numbertuple
print(combinetuple)