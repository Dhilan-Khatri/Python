mydict={
    "Name": "Billy",
    "Age": 62,
    "City": "Tokyo"
}
print(mydict)
#print(mydict["Name"])
#mydict.pop("City")
#print(mydict)
#print(mydict.get("Name"))
#mydict.clear
#print(mydict.popitem())
#del mydict
#print(mydict)
print(len(mydict))
print(mydict.values())
for i in mydict:
    print(i)
for key, value in mydict.items():
    print(key)
    print(value)