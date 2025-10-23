import random

length = int(input("Enter how long you want your password to be: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/|~"

password = (random.choices(characters, k=length))
print("Your random password is:", password)

random.shuffle(password)
final_password = ''.join(password[:length])
print("\nYour generated password is:", final_password)
