#list comprehension
X=[1,2,3,4,5,6]
newlist=[i for i in X if i%2==0]
print(newlist)

#dictionary comprehension
Num=[1,2,3,4,5,6]
newdict1={str (i):i**2 for i in Num}
print(newdict1)
newdict2={str (i):i**2 for i in Num if i%2!=0}
print(newdict2)

#math
Number1=[1,2,3]
Number2=[4,5,6]
newList=map(lambda x,y:x+y, Number1, Number2)
print(list(newList))
newList2=map(lambda x,y:x*y, Number1, Number2)
print(list(newList2))
Number3=[1,2,3,4,5]
def sq(n):
    return n*n
newList3=list(map(sq,Number3))
print(newList3)
def cube(n):
    return n*n*n
newList4=list(map(cube,Number3))
print(newList4)

#zip
name=["Bill", "Saketh", "Will", "Kim"]
id=[4,7,3,2]
Newlist1=list(zip(name, id))
print(Newlist1)

#exit
age=[90,45,12,70,90]
for i in age:
    if i <18:
        print(i,"Not Allowed")
        print(exit)
        exit()
    else:
        print(i, "Age is Allowed")