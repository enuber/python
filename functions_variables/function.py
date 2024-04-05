# def stands for define, allows you to create your own functions. 
# def means you are defining a function, this is followed by the name of the function, the () can allow arguments to be passed in and, then the : means everything after this that is indented is now apart of that function when it is called

# if you want the value to have a default, you can define it in the argument list

# the function is not hoisted. the function must must be defined before it is used.

# def hello(to="world"): 
#   print(f"hello, {to}")

# hello() # will be hello, world
# name = input("What's your name? ")
# hello(name) # will be hello, <name>

# by convention, you can put your body code into a function called main which means other functions can be on the page that called later. When you eventually call main everything else is already now defined so alleviates where things need to actually be in order.

# scope - a variable is only available in the scope for which it was created. If name wasn't being passed into the hello function and you tried to call name from hello you would get an error as name is not defined. 

# return - when we want to send back a value from a function you use return.

# def main():
#   name = input("What's your name? ")
#   hello(name) # will be hello, <name>

# def hello(to="world"): 
#   print(f"hello, {to}")

# main()


def main():
  x = int(input("what is X? "))
  print("x squared is", square(x))

def square(n):
  return n * n 

main()