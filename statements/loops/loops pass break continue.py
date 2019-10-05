
# break - breaks out of current closest enclosing loop
# continue - goes to the top of the closest enclosing loop
# pass - does nothing at all

# PASS
# x = [1,2,3]
# for num in x:
#     # comment SyntaxError: unexpected EOF while parsing

x = [1,2,3]
for num in x:
    # comment no error
    pass

print ('end of script')

# CONTINUE
mystring = 'sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter) # smmy

# BREAK
mystring = 'sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter) # s

x = 0
while x < 5:
    if x == 2:
        break # 0 1 !2 nie bo break domyka przedział
    print(x)
    x += 1