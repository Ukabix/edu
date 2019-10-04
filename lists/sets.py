# unordered collections of unique elements =< 1 of same object

myset = set() # set
print(myset)

myset.add(1)
print(myset)

myset.add(2)
print(myset)

myset.add(2) # no error
print(myset)

mylist = [1,1,1,1,1,2,2,3,3,3] # funkcjonalność w wyszukiwaniu 
print(set(mylist))