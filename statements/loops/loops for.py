# execute a block of code for every iteration

#syntax:
my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print('hello')


for num in mylist:
    # Check even
    if num % 2 == 0:
        print(num)
    else:
        print(f"odd number {num}")


list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

print(list_sum)


#strings
mystring = 'hello world'
for letter in mystring:
    print(letter)


for _ in mystring:
    print("Cool")


#tuple
mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for item in mylist:
    print(item)


#tuple unpacking!!!
mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for a, b in mylist:
    print(a)
    print(b)


mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a, b, c in mylist:
    #print(a)
    print(b)
    #print(c)


#dict
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)


for item in d.items():
    print(item)


for key, value in d.items():
    print(value)