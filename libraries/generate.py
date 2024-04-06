# docs.python.org/3/library/random.html
# import allows you to import modules, or libraries into a program

# random is a library that comes with python but has to be brought in
# by calling random here it is bringing in the entire library
# to then call these you have to use in this case random.functionname in order to use it.
# by adding from keyword, we can pull out what we want to use. this means to now call it, we can just call it by it's name. 
# why you would use one vs other. If you want your own function or variable called choice, you would keep it with random so it differentiates called random.choice versus your own which would then be choice.

import random
# from random import choice

# choice is a function in random library that takes a sequence, which is a list
coin = random.choice(['heads', 'tails']) 
# coin = choice(['heads', 'tails']) 

print(coin)

#random number from two digits
number = random.randint(1, 10)

print(number)

# shuffle things like a deck of cards, in random order in this case it mutates the list and reorders the list

cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
  print(card)


