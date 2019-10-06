# syntax
# def name_of_f():
#     '''
#     DOCSTRING: info
#     INPUT: expected
#     OUTPUT: expected
#     '''
#     print("something")
# print(name_of_f())
# help(name_of_f)
# () - function does not take args

def say_hello(name='NAME'): # default arg
    return("hello " + name)
# say_hello()
# say_hello('sally')
result = say_hello('Jose')
print(result)

def add(n1, n2):
    return n1 + n2
result = add(20, 30)
print(result)

# find out if "dog" is in a string - niepotrzebnie poprzez if ("dog" in mystring returns T/F)
def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
print(dog_check("my Dog run away"))
# wersja poprawna i krótka
def dog_check(mystring):
    return 'dog' in mystring.lower()
print(dog_check("my Dog run away"))

# pig latin
# word starts with vowel - add "-ay" / apple -> appleay
# word does not start with a vowel - first letter to end + "-ay" / word - ordway

def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in "aeiouy":
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin('word'))
print(pig_latin('apple'))
