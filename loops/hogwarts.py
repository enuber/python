# lists

students = ['Harry', 'Hermione', 'Ron', "Draco"]

# behaves like arrays where first item in list is 0

print(students[0]) # gives Harry

for student in students:
  print(student) # will print each student name without knowing how many in list

# len() will give you length of list so below we get the length of the list and then use that as the range. Remember range starts at 0 and goes up to but doesn't include the final number. So in this case even though length of list is 3 we would get 0, 1, 2
for i in range(len(students)): 
  print(i + 1, students[i]) 

# dict - dictionaries. this is a data type that lets you associate one variable with another, keys and values (basically an object)
  
# students = {
#   "Hermione" : "Gryffindor",
#   "Harry" : "Gryffindor",
#   "Ron" : "Gryffindor",
#   "Draco" : "Slytherin",
# }
  
# # in dictionaries you use the key to get the value
# print(students["Hermione"]) 

# for student in students:
#     print(student) # will see the keys

# for student in students:
#    print(student, students[student], sep=", ") # will see key followed by the value    

# None is a special word that means just that
students = [
  {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
  {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
  {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
  {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
   # will give back their names, houses and patronus as expected
  print(student['name'], student['house'], student['patronus'] sep=", ")