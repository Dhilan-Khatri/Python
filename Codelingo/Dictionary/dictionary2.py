dict={
    "Codingal": 2,
    "Is":2,
    "Best":4,
    "For":2,
    "Coding":1
    }
num=0
check=int(input("Checking for 1 or 2 or 4: "))
for key, value in dict.items():
    print(value)
    if value==check:
        num+=1
print(f"The Number {check  } Appears {num} times.")