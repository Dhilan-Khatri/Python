#5 input into list
# calulate avg
list=[]
sum=0
pro=1
for i in range (5):
    num=int(input("Enter the Number: "))
    list.append(num)
for i in list:
    sum+=i
    pro*=i
avg=sum/5
print(f"The Average of those 5 numbers is {avg}.")
print(f"The Product of those 5 numbers is {pro}.")
list.sort()
print(list)