myset={1,2,2,3,3,5,5,5}
print(myset)
myset.add(7)
print(myset)
myset1={5,6,7,8}
print(myset.intersection(myset1)) #same
print(myset.union(myset1)) #both
print(myset.difference(myset1)) #difference
print(myset.symmetric_difference(myset1)) #different
# print(myset[3]) Indexing not allowed in sets
