
# IN:

print('x' in [1,2,3])
print('x' in ['x', 'y','z'])

# RANGE
mylist = [1,2,3]

# range for iteration
for num in range(10):
    print(num)

for num in range(3, 10):
    print(num)

for num in range(3,10,2):
    print(num)

# range == generator
print(list(range(0,11,2)))
