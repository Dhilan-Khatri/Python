import array as arr

myarray=arr.array("i", [1,2,3,4])
print(myarray)
for i in range(4):
    print(myarray[i])
myarray1=arr.array("d", [1.0, 2.5, 4.6])
for i in range(3):
    print(myarray1[i])