# wywołanie bez domyślnego arg:
def get_integer(help_text):
  return int(input(help_text))
age = get_integer("Tell me your age: ") # tutaj zwróci podany tekst
school_year = get_integer("What grade are you in? ") # tutaj zwróci podany tekst
if age > 15:
  print("You are over the age of 15")
print("You are in grade " + str(school_year))

# wywołanie z domyślnym arg
def get_integer(help_text="Give me a number: "): # tutaj zwróci podany tekst
    return int(input(help_text)) # tutaj zwróci domyślny tekst
age = get_integer("Tell me your age: ")
school_year = get_integer()
if age > 15:
    print("You are over the age of 15")
print("You are in grade " + str(school_year))
