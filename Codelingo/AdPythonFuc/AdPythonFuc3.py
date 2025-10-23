
num = int(input("Enter a number: "))

odd_numbers = [x for x in range(num) if x % 2 != 0]
even_numbers = [x for x in range(num) if x % 2 == 0]
print("\nOdd numbers under", num, ":", odd_numbers)
print("Even numbers under", num, ":", even_numbers)



fruits = ["apple", "banana", "mango", "cherry", "grape", "orange", "melon"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("\nUncapitalized fruits list:", fruits)
print("Capitalized fruits list:", capitalized_fruits)
