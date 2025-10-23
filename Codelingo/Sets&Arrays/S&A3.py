#make element[1,3,5,3,7,9,3]
#find accoruance of 3 in array
#reverse arrangement
import array as arr

num=arr.array("i", [1,3,5,3,7,9,3])
num2=arr.array("i", []) 
x=0
ct=0
for i in num:
    if i==3:
        ct+=1
print(f"The number of times #3 appears is {ct}.")

for i in range(len(num)-1,-1,-1):
    x=num[i]
    num2.append(x)
print(num2)
#or
num3=arr.array("i", num[::-1])
print(num3)