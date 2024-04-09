# class methods - it isn't necessary to associate a function with objects of a class but with the class itself. Doesn't matter what the own values or instant variables are
# @classmethod - used to specify that this method is not by default an instance method with access to self but it knows what class it is inside. can therefore use a class as a container for data or functionality that is related to something. Pass in the reference to the class itself which is what cls is, this has to be this keyword.
# when should you use a class - when you are trying to represent an entity. Like a student, or sorting hat. 
# class variables - are variables that aren't apart of the the __init__ and there is just one copy for all the objects they all share the same variable. Doesn't use "self" as no longer relevant it refers to specific objects. So a class variable is good regardless of what object it is in. ie Not unique. 

import random

class Hat:

  houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  @classmethod
  def sort(cls, name):
    house = random.choice(cls.houses)
    print(name, "is in", house)

def main():
  # no longer have to instantiating an object of type Hat because there is nothing unique about it. Can just call it just like we would int() or str()
  Hat.sort("Harry")

if __name__ == "__main__":
  main()