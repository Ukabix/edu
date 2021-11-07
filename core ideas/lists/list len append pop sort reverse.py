# my_list = [1, 2, 3]

my_list = ['string', 100, 21.2]

print(len(my_list))

mylist = ['one', 'two', 'three']

print(mylist[0]) # index
print(mylist[1:]) # slice

another_list = ['four', 'five']

print(mylist + another_list)

new_list = mylist + another_list

print(new_list)

new_list[0] = 'ONE' # mutate

print(new_list)

new_list.append('six')

print(new_list)

new_list.pop()

print(new_list)

popped_item = new_list.pop()

print(new_list)
print(popped_item)

popped_item = new_list.pop(0)

print(new_list)
print(popped_item)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()
print(new_list)

# new_list.sort() = my_sorted_list
# type(my_sorted_list) # None
# print(my_sorted_list) # pusta, bo .sort nie ma żadnego return

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)