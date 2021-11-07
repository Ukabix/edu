mylist = [1,2,3]

myset = set()

# class creation
class SampleClass():
    pass

my_sample = SampleClass()

print(type(my_sample))

# class attributes
class Dog():

    def __init__(self, mybreed, name, spots):
        # Attributes
        # We take in the argument
        # assign it using self.attribute_name
        self.mybreed = mybreed
        # same as self.my_attribute = mybreed
        self.name = name
        # Expecting T/F \/
        self.spots = spots


my_dog = Dog(mybreed= 'garman shepherd', name= 'Jupiter', spots= False)

print(type(my_dog))
print(my_dog.mybreed) # same as print(my_dog.my_attribute)
print(my_dog.name)
print(my_dog.spots)


# my_sample = SampleClass1()
#
# print(type(my_sample))

