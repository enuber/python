# issue with this is if the user enters something that is not a number or not an integer
# typing in a word instead of a number gives a valueError: invalid literal for int() with base 10:
# a literal is what was typed in, in this case. 
# we need to write code with error handling in mind. For unexpected situations. Need to program defensively

# x = int(input('What\'s X? '))
# print(f"x is {x}")

# try - allows you to try something to see if something erronious has happened. 
# except - if try something can do an except if something does go wrong. so can set it to an error type and handle that error
# there is an exception to catch all but, this may hide other bugs. So figuring out what kind of errors could happen it is better to find cases and handle them.
# you should only be trying code in 'try' that can actually fail in some way. Here we have print that is likely not to fail so shouldn't be included. 

# try: 
#   x = int(input('What\'s X? ')) 
#   print(f"x is {x}")
# except ValueError:
#   print("x is not an integer")


# NameError - usually refers to an error in a something in your code that is named incorrectly or not defined.
# this code is now bugged based on if x is an int or not. Because if x is a string, x is then never defined as being anything because the error happens and the except portion runs. So when the next line of print() happens outside of the except, x is not defined and throws a NameError
# else allows you to fix this by putting in else at the end, if the except runs then the else won't if the except doesn't run then the else will.  Else only happens if the try happened and succeeded

# try: 
#   x = int(input('What\'s X? ')) 
# except ValueError:
#   print("x is not an integer")
# else:
#   print(f"x is {x}")  

# adding a loop in this is better as we are trying to get an integer. remember break is a keyword that forces the loop to end.

# while True:
#   try: 
#     x = int(input('What\'s X? ')) 
#   except ValueError:
#     print("x is not an integer")
#   else:
#     break
# print(f"x is {x}") 

# further refine note that here we get rid of break as return will return from the function that is stronger than break. Loop will still be ended. Also shortened it up because we don't need to define a value just to pass it back out, we can just return what was being prompted to further shorten the code. 

# def main():
#   x = get_int()
#   print(f"x is {x}") 

# def get_int():
#   while True:
#     try: 
#       return int(input('What\'s X? ')) 
#     except ValueError:
#       print("x is not an integer")
  
# main()

# pass - if you don't want to do anything if something fails you can just pass it. pass is a keyword. It may be more userfriendly as it will keep asking what x is but, then it also isn't telling people why their value isn't working. So need to decide what is best.

# def main():
#   x = get_int()
#   print(f"x is {x}") 

# def get_int():
#   while True:
#     try: 
#       return int(input('What\'s X? ')) 
#     except ValueError:
#       pass
  
# main()

# better even to pass in the info we want to get into the function. makes the function more reuseable as well. Makes it so you can reuse and ask for Y or Z...etc so makes it better.

def main():
  x = get_int("What's X? ")
  print(f"x is {x}") 

def get_int(prompt):
  while True:
    try: 
      return int(input(prompt)) 
    except ValueError:
      pass
  
main()