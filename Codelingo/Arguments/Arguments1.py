
def pay(tip, bill):
    total = bill*(1+0.01*tip)
    total=round(total,2)
    return total

bill= int(input("Enter The price of the bill: "))
tip= int(input("Enter the amount to tip: "))

totalamt= pay(bill, tip)
print(f"Total Amount to Pay is {totalamt}")