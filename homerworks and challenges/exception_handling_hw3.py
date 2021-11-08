### Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a <code>while</code> loop with a <code>try</code>, <code>except</code>,
#  <code>else</code> block to account for incorrect inputs.

def ask():
    
    while True:
        try:
            a = int(input("please provide a number"))
        except:
            print("not a number, please try again\n")
            continue
        else:
            b = a**2
            print(b)
            break
ask()