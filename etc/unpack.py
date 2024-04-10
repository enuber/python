# unpacking - similar to below were we are destructing

# first, last = input("what's your name? ").split(" ")
# print(f"hello, {first}")

# def total(galleons, sickles, knuts):
#   return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# # this will unpack the list. so now will be the individual numbers in the list.
# print(total(*coins), "Knuts")




# def total(galleons, sickles, knuts):
#   return (galleons * 17 + sickles) * 29 + knuts

# coins = {
#   'galleons':100, 
#   'sickles':50, 
#   'knuts':25
# }

# this will unpack the dictionary. this will unpack so we have galleons=100, sickles=50, knuts=25. Will pass in all the keys and all the values with = bewteen and , so it will set it up as expected.
# print(total(**coins), "Knuts")




# *args, **kwargs - can be used as indicator when a function may take a variable number of arguments.

# here we will take a positional number of arguments where the arguments go from left to right. 
# #kwargs - keyword arguments. named parameters that can be called individually by their own name.
def f(*args, **kwargs):
  print("Positional:", args)
  print("Names:", kwargs)

f(100, 50, 25) # <- will give Positional: (100, 50, 25)
f(galleons=100, sickles=50, knuts=25) # <- gives us Names: {'galleons': 100, 'sickles': 50, 'knuts': 25}

  