### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

#for i in ['a','b','c']:
#    print(i**2)

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("we have a TypeError")
finally:
    print("we have handled the exception")