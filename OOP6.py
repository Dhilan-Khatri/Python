#class = find mun in tuples that adds up to sum and returns pos of element, value of sum can be given as imput of user.
#tuple(10,20,30,40,50,60,70) 

tuple1=(10,20,30,40,50,60,70)
class findnums():
    def __init__(self, sum):
        self.sum=sum
    def find_Nums(self):
        for i in range(len(tuple1)-1):
            if i < len(tuple1)-2:
                if tuple1[i]+tuple1[i+1]==self.sum:
                    print(f"The Numbers That Make {self.sum} is {tuple1[i]} and {tuple1[i+1]}")
sum=int(input("Enter A Number that is a mutiple of 10, up to 130: "))
obj1=findnums(sum)
obj1.find_Nums()