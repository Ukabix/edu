# immutable, data integrity

t = (1,2,3)
mylist = [1,2,3]
print(type(t))
print(type(mylist))

t = ('one', 2)
print(t[0])
print(t[-1])

# metody

t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))

# t[0] = 'new' # TypeError: 'tuple' object does not support item assignment