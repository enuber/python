# with the basic class we had in part 2 we can still access the Student class through dot notation. So even with some basic checks we can still do what we want with dot notation. So can override house to be the actual place a student grew up in. 

# properties - an attribute with more functionality so people can't mess things up. 
# @property - is the keyword which is a function 
# decorators - functions that modify the behaviour of other functions

# by defining getters and setters when outside the class the dot notation is called for assigning or getting a variable, instead, it will automatically call the associated function. so student.house will call the getter and student.house="something" will call setter.

class Student: 
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing name")
    # no longer need this here because using a getter/setter it will automatically call those therefore the error handling is in the setter already. This is because we are doing the self.house="something" here too.
    # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #   raise ValueError("Invalid House")
    self.name = name 

    # the variable and function can't be called the same thing. So either this can be called house or the getter can be called house because python will confuse one for the other. To fix this, in the getter and setter by convention we use _ before the name. so _house. So the instance variable is called _house but the property is called house.
    self.house = house

  def __str__(self):
    return f"{self.name} from {self.house}"
  
  # getter - a function that gets some attribute
  # tells python to use this as a getter, the function must be the property as it is called.
  @property
  def house(self):
    return self._house
  
  # setter - a function that sets some attribute
  # tells python to treat has setter, by creating the getter, it then creates this decorator that is @<gettername>.setter that sets up the setter.
  @house.setter
  def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House")
    self._house = house

def main():
  student = get_student()
  # student.house = "Number Four, Privet Drive"
  print(student)


def get_student():
  name = input("Name? ")
  house = input("House? ")
  return Student(name, house)


if __name__ == "__main__":
  main()