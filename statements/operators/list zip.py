
# ZIP
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']

zip(mylist1, mylist2) # return None

for item in zip(mylist1, mylist2):
    print(item) # return tuple

# 3 elements
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [111, 222, 333]

zip(mylist1, mylist2, mylist3) # return None

for item in zip(mylist1, mylist2, mylist3):
    print(item)
    # return tuple
    # return output tuple.len = shortest list.len

# list generation:
print(list(zip(mylist1, mylist2, mylist3)))
