# Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.
# Then use a <code>finally</code> block to print 'All Done.'

# x = 5
# y = 0

# z = x/y

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("we have a ZeroDivisionError")
finally:
    print("we have handled the ZeroDivisionError")
