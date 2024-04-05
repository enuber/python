# loops allow us to go through code multiple times based on a condition

# while is one way we can express a loop and uses a boolean to decide to cotinue or not

i = 3

while i != 0:
  print('meow')
  i = i - 1


i = 0

while i < 3:
  print('woof')
  # this is more succinct and does i = i + 1 with slightly less code
  i += 1


# for loops allows you to go through a list of items and do something
# list is a type and is what is between the []. (ie an array in JS)
# range(3) this is a function that will go from 0 up to but not include the number in the () so this would give 0, 1, 2. This would help allow for extreme cases. 

for i in [0, 1, 2]:
  print(i)

for i in range(3):
  print('meow')

# if you need a variable but don't actually use it or does anything you use an underscore instead. so above would be written as 
  
# for _ in range(3):
#   print('meow')


# this can be simplified so we can print it out three times by multiplying. To get each meow on a new line we use the \n and so we don't get the final new line, we use end="" so that the last meow will not execute the new line.
print('meow\n' * 3, end="");


# here is a way to get a user to input a positive integer. If not positive will keep asking. Continue is a keyword that means just keep going. Break is a keyword that will break out of the loop.

# while True:
#   n = int(input("What's n? "))
#   if n < 0 :
#     continue
#   else: 
#     break

# can shorten this but above is to show the new keywords

while True:
  n = int(input("What's n? "))
  if n > 0 :
    break

for _ in range(n):
  print('meow')  