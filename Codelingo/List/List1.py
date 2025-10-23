list1=[1,2,3,4,5,6,7,8,9,0]
list2=["Good Morning","How Are you?"]
list3=[True, False]
print(list1)
print(list2)
print(list3)
print(len(list1))
print(list1[7])
person=["bill", 8, "USA", 40.5, True]
print(person[2])
print(person[0:3])
for i in person:
    print(i)
list4=list1+list2+list3
print(list4)
list4.extend(person)
print(list4)
person.append(1000)
print(person)
print(person[::-1])