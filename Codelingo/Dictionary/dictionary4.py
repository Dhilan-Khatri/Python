dict={
    "Codingal": 3,
    "Is":2,
    "Best":2,
    "For":2,
    "Coding":1
    }
num=0
check=int(input("Checking for 1 or 2 or 3: "))
for key, value in dict.items():
    if value==check:
        num+=1
print(f"The Number {check} Appears {num} times.")