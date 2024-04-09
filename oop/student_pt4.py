# after hat.py


class Student: 
  def __init__(self, name, house):
    self.name = name 
    self.house = house

  def __str__(self):
    return f"{self.name} from {self.house}"
  
  # can call this method without instantiating the class first.
  @classmethod
  def get(cls):
    name = input("Name: ")
    house = input("House: ")
    # returns a new Student object by calling cls passing in name and house as cls is a reference to the class itself, so it's calling itself basically passing in the things we need to instantiate it.
    return cls(name, house)

def main():
  student = Student.get()
  print(student)


if __name__ == "__main__":
  main()