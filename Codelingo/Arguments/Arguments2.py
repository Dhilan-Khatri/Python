#func1 find cube of a number
#func2 if num is disviable by 3

def func1(num):
    cube=num**3
    return(cube)

def func2(num):
    if num%3 ==0:
        return func1(num)
    else:
        return("Give Another Number")

num=int(input("Enter An Number: "))
result=func2(num)
print(result)