import csv

# csv is a very common file type, comma separated values, allows us to store multiple types of data in a line to make it more useful. 

# with open('./students.csv') as file:
#   for line in file:
    # row here will hold all the values that were split by a comma so captures an entire row and, this would hold any number of values.
    # row = line.rstrip().split(',')
    # print(f"{row[0]} is in {row[1]}")

    # doing it with knowing what the info is. 
    # name, house = line.rstrip().split(',')
    # print(f"{name} is in {house}")



# sorting
students = []

# this works but, only because student name is first. 
# with open('./students.csv') as file:
#   for line in file:
#     name, house = line.rstrip().split(',')
#     students.append(f"{name} is in {house}")

# for student in sorted(students):
#   print(student)

# with open('./students.csv') as file:
#   for line in file:
#     name, house = line.rstrip().split(',')
#     # student = {}
#     # student['name'] = name
#     # student['house'] = house
#     # does the same thing as above but in one line vs. three
#     student = {"name": name, "house": house}
#     students.append(student)

# can switch this to get_house and return student['house'] to also get list sorted by house. the sorted funtion is called and, by returning the student from this get_name function, it is being told we want to sort by name so it sorts properly.

# def get_name(student):
#   return student['name']

# sorted can take a key to sort by. allows us to sort by either name or house in this case. You do not use get_name(), just the name of the function.
# in this case the key is a function where when called, gets the student and returns the
# we can pass a function as arguments into other functions. 

# for student in sorted(students, key=get_name, reverse=True):
#   print(f"{student['name']} is in {student['house']}")


# instead of passing key a name of a function, you can do this with an annoymous function
# lambda - says to python that a function is coming but it has no name. That function takes a parameter, in the case below "student", what do you want returned, you want to go into that dictionary and access their name, so the sorted function uses those names to decide how to sort.

# for student in sorted(students, key=lambda student: student['name'], reverse=True):
#   print(f"{student['name']} is in {student['house']}")


# in the studeents.csv file we have a name that has a home that has a comma in it. The way the code is now, this is a problem because it wil break thde code.
# there is a module called csv. (note: imported at very top of file)
# now we need to iterate over the reader not the file itself. 


# with open('./students.csv') as file:
#   reader = csv.reader(file)
#   # now we need to iterate over the reader not the file itself. 
#   # can also unpack the info here so don't have to use the row[0] and row[1]
#   # for row in reader:
#   for name, home in reader:
#     # the returned row is a list. so we have to use the list syntax
#     # students.append({"name": row[0], "home": row[1]})
#     students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student['name'], reverse=True):
#   print(f"{student['name']} is in {student['home']}")    


# now using a file with name,home as first row that says what the columns are.
# by doing this as a DictReader, if the file is ever changed as long as the top row gives us what is in each column, this code won't break as with a list, it must be in a specific order.

with open('./students.csv') as file:
  # this will now read the file line by line as a dictionary of columns instead of a list of columns. Will give me access to those column names
  reader = csv.DictReader(file)
  for row in reader:
    # had to change this line because we no longer have a list but a dictionary
    students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student['name'], reverse=True):
  print(f"{student['name']} is in {student['home']}")    