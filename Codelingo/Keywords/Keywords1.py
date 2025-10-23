#return keyword
def func(a,b):
    return a+b
print(func(1,2))
print("/n")
#continue keyword
for i in range(10):
    if i%3==0:
        continue
    print(i)
print("/n")
#break keyword
for i in range(1,10):
    if i%3==0:
        break
    print(i)
print("/n")
#pass keyword
a=10
b=20
if a<b:
    pass
else:
    print(b<a)