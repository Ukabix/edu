import os

for item in os.listdir("."):

    if os.path.isfile(item):
        print("{} jest plikiem".format(item))

    if os.path.isdir(item):
        print("{}jest folderem".format(item))

