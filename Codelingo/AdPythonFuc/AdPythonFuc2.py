list1=[10,20,30,40]
list2=[100,200,300,400]

list3=list(zip(list1, list2[::-1]))
print(list3)

stock=["meta", "google", "tesla"]
price=[2517, 234, 5]
newdict={stock:price for stock, price in zip(stock,price)}
print(newdict)
print(zip(stock,price))