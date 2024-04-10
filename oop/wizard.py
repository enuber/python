# inheritance - one class can inherit attributes methods/variables from another class
# multiple class relate to eachother, they have some heirarchy
# 

# in our case both students and professors are wizard so we can have a main class
# Wizard is the super class and by adding Student(Wizard) we are saying to Student class to inherit everything from Wizard.

class Wizard: 
  def __init__(self, name):
    if not name:
      raise ValueError("Missing name")
    self.name = name
    
  ...

class Student(Wizard): 
  def __init__(self, name, house):
    # calls the super class which in a reference to the Wizard class.
    super().__init__(name)
    self.house = house

  ...

class Professor(Wizard):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject

  ...

student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence Against the Dark Arts")
wizard = Wizard("Albus")