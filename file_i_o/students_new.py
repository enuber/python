import csv

name = input("what's your name? ")
home = input("where's your home? ")

# writing to a file with csv.
# use csv.writer(file) returns a value of the function that creates the file 
# write.row() - takes it as a list and puts the info into the .csv 
# note that if you were to type a name, home with a comma in it, it will automatically get quotes in the .csv file.

# with open('students_new.csv', 'a') as file:
#   writer = csv.writer(file)
#   writer.writerow([name, home])

# can also do this as a DictWriter which uses a dictionary so we don't have to be concerned with order of how things get put in

with open('students_new.csv', 'a') as file:
  # need to include fieldnames to let the writer know the names of the columns in the file.  
  writer = csv.DictWriter(file, fieldnames=["name", "home"])
  # this could be switched up home then name as the above makes sure the info goes into the correct area.
  writer.writerow({"name": name, "home": home})