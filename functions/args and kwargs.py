def myfunc(a,b): # a,b - positional arguments
    # returns 5% of a+b
    return sum((a,b)) * 0.05

print(myfunc(40,50))

# *args(conv)/*anykeyword - allows the function to take an arbitrary amount of arguments
def myfunc1(*args):
    print(args) # tupla
    return sum(args) * 0.05

print(myfunc1(40,50,1,22,54,66,7774,332,2))

def myfunc2(*args):
    for item in args:
        print(item) # tupla

myfunc2(12,2,2,15,22)

# **kwargs builds a dict

def myfunct3(**kwargs):
    print(kwargs) # dict
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("no fruits here")

myfunct3(fruit='apple', veggie='potato')

# combo

def myfunc4(*args, **kwargs):
    print(args) # tupla
    print(kwargs) # dict
    print("I would like {}{}".format(args[0],kwargs['food']))

myfunc4(10,20,30,fruit='orange', food='eggs', animal='dog') # !position of args, kwargs