# class is a blueprint for pieces of data. Like a mould give it a name and has types of data that are designed exactly as you want. They let you design your own datatypes. 
# objects - when you use the class you are creating objects.
# attributes - are instance variables
# methods - functions inside of a class
# __init__ - can customize the classes object. it is an instance method. Designed to initialize the contents of an object in a class.
# self - has to come first, gives you access to the current object that was just created
#   this installs into the empty object in identically name instance variables. The object is just an instance of the class.
# self.name, self.house - adding variables to objects. 
# raise - a way to throw or "raise" an error, lets the "programmer" know there was a problem. 
# can control what is being installed into the object. 

#__str__ - special method will be called automatic when anytime some other function wants to see a string.  Like print

# can create your own methods, a function built into it. Always has self coming into it so you have access to the current object

class Student: 
  def __init__(self, name, house, patronus):
    if not name:
      raise ValueError("Missing name")
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House")
    self.name = name 
    self.house = house
    self.patronus = patronus

  def __str__(self):
    return f"{self.name} from {self.house}"
  
  def charm(self):
    match self.patronus:
      case "Stag":
        return "🦌"
      case "Otter":
        return "🦦"
      case "Jack Russell terrier":
        return "🐶"
      case _:
        return "🪄"



# to get back out the contents of the class is also using dot notation.
# because __self__ was created print will get back that sentence. 
def main():
  student = get_student()
  print(student)
  print("Expecto Patronum!")
  print(student.charm())
  print(f"{student.name} from {student.house}")

def get_student():
  # appears to be calling a function, but we are calling the class
  # to put a new attribute inside the student class.
  # student is an object of the class Student.

  # student = Student()
  # student.name = input("Name? ")
  # student.house = input("House? ")

  # this is different... now passing info into the Student class. This way we have more control over the class
  # We are treating Student() as a function passing in name and house. It is a constructor call in this case. It is going to instantiate a students object. It is going to use the class as a "mould". Because you can pass in arguments into the function you can customize the contents of that object. It is a Student blue print that we can use to build different objects as long as we are passing in a name and house which can be different. Where is this function? It is the __init__ that is being called which is the initialization of the object. 
  # can use a try / except to create the Student and in the class it may throw the error if something isn't correct.
  name = input("Name? ")
  house = input("House? ")
  patronus = input("Patronus? ")
  # try: 
  return Student(name, house, patronus)
  # except ValueError:


if __name__ == "__main__":
  main()