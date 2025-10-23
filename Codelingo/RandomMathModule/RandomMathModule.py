#user gives num 1-10
#save ran num 1-10
#if equal print "Winner"
#Else "Loser"
from random import *
user=int(input("Give a number 1-10: "))
num=randint(1,10)
print(f"Commputer Number is {num}")
if user == num:
    print("Winner")
else:
    print("Loser")
