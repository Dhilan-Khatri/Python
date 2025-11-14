#write from user (word & def) = 1 obj
# to assign word & meaning used flashcard
#use __str__ to format (word, meaning)
#add all obj(s) into a list
#at end use for loop to print all

class assign:
    def __init__(self, word, mean):
        self.word=word
        self.mean=mean
    def __str__(self):
        return self.word+" : "+self.mean
x=0
flashcard=[]
while x==0:
    word=input("Enter a word: ")
    meaning=input("Enter the meaning: ")
    flashcard.append(assign(word, meaning))
    ans=input("Do you want to make more? (y/n)")
    if ans == "n":
        x=1

for i in flashcard:
    print(i)

