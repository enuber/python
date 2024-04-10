# set - a collection of values where there are no duplicates. useful if you want to automatically filter out dupes.

students = [
  {"name": "Hermione", "house": "Gryffindor"},
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Ron", "house": "Gryffindor"},
  {"name": "Draco", "house": "Slytherin"},
  {"name": "Padma", "house": "Ravenclaw"},
]

# this is doing it programatically
# houses = []

# for student in students:
#   if student["house"] not in houses:
#     houses.append(student["house"])

# for house in sorted(houses):
#   print(house)


# doing it as a set
houses = set()

for student in students:
  # add is used to put something into a set.
  houses.add(student["house"])

for house in sorted(houses):
  print(house)
