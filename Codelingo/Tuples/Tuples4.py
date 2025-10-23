tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

tup = int(input("Do you want Tup1 or Tup2? Please enter either 1 or 2: "))

def tuple_product(t):
    product = 1
    for i in t:
        product *= i
    return product

if tup == 1:
    result = tuple_product(tup1)
    print("Product of tup1:", result)

elif tup == 2:
    result = tuple_product(tup2)
    print("Product of tup2:", result)
    
else:
    print("Invalid input. Please enter 1 or 2.")
