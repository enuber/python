# constants - can not be changed, we can do things to get around it but, generally it is difficult and shoudln't be done. Python doesn't actually do this so it's on honor system.
# convetion is to captialize the word.

# TIMES_TO_MEOW = 3

# for _ in range(TIMES_TO_MEOW):
#   print("meow")

# here it is in a class, it is same thing. convetion to uppercase it. 
# class Cat:
#   MEOWS = 3

#   @classmethod
#   def meow(cls):
#     for _ in range(Cat.MEOWS):
#       print("meow")

# Cat.meow()

# type hints - hints that let python know what things should be. 
# mypy - pip install mypy is a tool that allows you to check your type hints.
# n: int - this is a type hint3
# -> None - this is the type hint that tells you what the code is returning. When a function doesn't return anything it actually returns None.
# this means when I am trying to get a return value from the function it will be caught by mypy as not actually returning anything. So would know to fix it.
# def meow(n: int) -> None:
#   for _ in range(n):
#     print("meow")

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(number)


# fix where we are now returning something.
# def meow(n: int) -> str:
#   return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

# docstrings - document strings, standardize way to how something should be documented. 

# def meow(n: int) -> str:
#   """ Meow n times. """ # this line is if you are commenting a line of code
#   """ 
#     Meow n times. 
#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeEror: if n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#   """

#   return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

# argparse
# when controlling from the command line you provide a switch or flags where you pass in like -n which means a number of times or could do --number if using the whole word.
# argparse - 

# import sys

# if len(sys.argv) == 1:
#   print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == '-n':
#   n = int(sys.argv[2])
#   for _ in range(n):
#     print("meow")
# else:
#   print('usage: meows.py')

# ArgumentParser - is a constructor comes with Python
# parse_args() - auto will look at sys.argv for us. Will do this itself. 
# args - gives us the object of all the command line arguments no matter what order they appear in.
# can run python meows.py -h - or --help and will give you information about what is expected. in our case we will get usage: meows.py [-h] [-n N]. [] means its optional in documentation. 
# by adding text of description= and help= we give the help window a bit more info.

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
# by giving the type here, it will handle making sure it's the correct type in the background so we don't have to do it later ourselves.
parser.add_argument("-n", default=1, type=int, help="number of times to meow")
args = parser.parse_args()

for _ in range(args.n):
  print("meow")