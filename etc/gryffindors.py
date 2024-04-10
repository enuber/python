# after unpack and yell

students = [
  {"name": "Hermione", "house": "Gryffindor"},
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Ron", "house": "Gryffindor"},
  {"name": "Draco", "house": "Slytherin"},
  {"name": "Padma", "house": "Ravenclaw"},
]

# gryffindors = [
#   student['name'] for student in students if student["house"] == "Gryffindor"
# ]
# for gryffindor in sorted(gryffindors):
#   print(gryffindor)

# filter - finds items that are "True" and returns only those.

# def is_gryffindor(s):
#   return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s['name']):
#    print(gryffindor["name"])



# dictionary comprehension - lets you build it all at once

# this is doing it ourselves programatically
# students_list = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students_list: 
#   gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)

#with dictionary comprehension

# students_list = ["Hermione", "Harry", "Ron"]

# # gryffindors = [{"name": student, "house": "Gryffindor"} for student in students_list]

# gryffindors = {student: "Gryffindor" for student in students_list}

# print(gryffindors)



# enumerate - iterate over a sequence, gives you both the value and index one at a time
# enumerate(iterable, start=0)

students_list = ["Hermione", "Harry", "Ron"]

# for i in range(len(students_list)):
#   print(i + 1, students_list[i])

for i, student in enumerate(students_list):
  print(i+1, student)