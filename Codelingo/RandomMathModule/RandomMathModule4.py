from random import *


#computer = int(randint(1,3))
#user= int(input("Choose 1 Option, Rock=1, Sissors=2, Paper=3: "))
#try:
    #if computer == user:
        #print("TIE")
    #if user ==1 and computer == 2:
      #  print("Winner")
  #  if user ==1 and computer == 3:
 #       print("Loser")
 #   if user ==2 and computer == 1:
 #       print("Loser")
 #  if user ==2 and computer == 3:
  #      print("Winner")
   # if user ==3 and computer == 1:
  #      print("Winner")
   # if user ==3 and computer == 2:
  #      print("Loser")
#except ValueError:
  #  print("Please Enter 1, 2, or 3.")

while True:
    user= int(input("Choose 1 Option, Rock=1, Sissors=2, Paper=3: "))
    list = ["Rock",  "Paper", "Sissors" ]
    computer= random.choice(list)
    print(f"Your choice was {user}. And the Commputer choice was {computer}")
    if user == computer:
        print("TIE")
    elif user == "rock":
        if computer== "sissors":
            print("Winner")
        else:
            print("Loser")
    elif user == "Sisscor":
        if computer== "Paper":
            print("Winner")
        else:
            print("Loser")
    elif user == "Paper":
        if computer== "Rock":
            print("Winner")
        else:
            print("Loser")