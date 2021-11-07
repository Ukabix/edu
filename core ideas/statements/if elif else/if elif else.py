# #syntax:
# if cond:
#     execute1
# elif:
#     execute3
# else:
#     execute2

if True:
    print("it's true")

if 3 > 2:
    print("it's true")

hungry = True

if hungry:
    print("feed me!")

hungry = False

if hungry:
    print("feed me!")
else:
    print("don't feed me")

loc = 'bank'
if loc == 'auto shop':
    print("cars are cool")
elif loc == 'bank':
    print("money is cool")
elif loc == 'store':
    print("welcome to the store")
else:
    print("i do not know much")

name = 'sammy'

if name == 'frankie':
    print("hi frankie")
elif name == 'sammy':
    print("hi sammy")
else:
    print("who are you?")
