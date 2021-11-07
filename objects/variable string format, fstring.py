# . format

print("this is a string {}".format("This is inserted"))

print("The {} {} {}.".format("fox", "brown", "quick"))

# operator porządkowy
print("The {2} {1} {0}.".format("fox", "brown", "quick"))

print("The {0} {0} {0}.".format("fox", "brown", "quick"))

# operator poprzez zmienną
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

print("The {f} {f} {f}".format(f="fox", b="brown", q="quick"))

# float formatting {value:width.precision f}
result = 100/777

print("the result was{r}".format(r=result))

print("the result was{r:1.3f}".format(r=result))

print("the result was{r:10.5f}".format(r=result))

# f strings - od 3.6
name = "Jose"
age = 3

print(f"Hello, his name is {name} and he is {age} y.o.")
