# > >= < <= == != comparisons
# if statement: use the colon to then show what you want to do if the comparison is true
# elif is short for else if
# else for last statement

x = int(input("what's x? "))
y = int(input("what's y? "))

if x < y:
  print('x is less than y')
elif y < x:
  print('y is less than x')
else:
  print('x and y are equal')

# or allows you to compare multiple things
  
if x < y or x > y:
  print('x is not equal to y')
else:
  print('x is equal to y')

# same as asking !=

if x != y:
  print('x is not equal to y')
else:
  print('x is equal to y')

# and similar to or, allows you to compare multiple things
  # see grade.py