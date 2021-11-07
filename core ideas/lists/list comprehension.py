# unique way to quickly create lists
# alternative to append

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

#ex1
mylist = [letter for letter in mystring]
print(mylist)

#ex2
mylist = [x for x in 'word']
print(mylist)

#ex3
mylist = [qwe for qwe in 'wordword']
print(mylist)

#ex4
mylist = [num**2 for num in range (0,11)]
print(mylist)

#ex5
mylist = [x for x in range(0,11) if x%2==0]
print(mylist)

#ex6
mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)

#ex7
cels = [0, 10, 20, 30, 40.5]
fahr = [((9/5)*temp + 32) for temp in cels]
print(fahr)

#ex7 as for loop
cels = [0, 10, 20, 30, 40.5]
fahr = []
for temp in cels:
    fahr.append((9/5)*temp + 32)
print(fahr)

#ex8 - if statements - interesting grammar
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)