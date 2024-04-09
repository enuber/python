# beginning of OOP
# class is a blueprint for pieces of data. Like a mould give it a name and has types of data that are designed exactly as you want. They let you design your own datatypes. 

def main():
  # name1 = get_name()
  # house2 = get_house()
  # name, house = get_student()
  # print(f"{name} from {house}")

  # student = get_student()
  # # if it's a tuple you can't change doing this, if it was a list in [] brackets you can
  # if student[0] == "Padma":
  #   student[1] = "Ravenclaw"
  # print(f"{student[0]} from {student[1]}")

  student = get_student()
  if student["name"] == "Padma":
    student["house"] = "Ravenclaw"
  print(f"{student['name']} from {student['house']}")

def get_name():
  return input("Name: ")

def get_house():
  return input("House: ")

# tuple - a collection of values. 
# returning two things from one function by separating by comma. 
# you aren't actually returning two things, you are returning one thing but it happens to be a tuple. You also don't have to put the () around it. A tuple is immutable
# 
# def get_student():
#   name = input("Name: ")
#   house = input("House: ")
#   return (name, house)

# with dictionary

def get_student():
  student = {}
  student["name"] = input("Name: ")
  student["house"] = input("House: ")
  return student

if __name__ == "__main__":
  main()