list1=["abc","cfc", "xyz", "aba", "1221", "a"]
#check list
#If lenght > 1
    #check if same backwards
        #increase counter by one
#print counter
c=0
list2=[]
for i in list1:
    if len(i) > 1:
        x=i[::-1]
        if x==i:
            list2.append(i)
            c+=1
print(c)
print(list2)