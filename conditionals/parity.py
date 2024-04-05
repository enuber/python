# % - represents modulo which is the remainder we have left

# x = int(input("what's x? "))

# if x % 2 == 0:
#   print('even')
# else: 
#   print('odd')


# def main():
#   x = int(input("what's x? "))
#   if is_even(x):
#     print('even')
#   else: 
#     print('odd')

# # booleans are capitalized  
# def is_even(n):
#   if n % 2 == 0:
#     return True
#   else: 
#     return False
  
# main()  



def main():
  x = int(input("what's x? "))
  if is_even(x):
    print('even')
  else: 
    print('odd')


def is_even(n):

  # more elegant and expected as it's "pythonic" 
  # return True if n % 2 == 0 else False

  # and even better because we are asking for a true or false to be returned
  # this is already asking if it's true or false so simplifies what you are saying even further
  return n % 2 == 0
  
main()  