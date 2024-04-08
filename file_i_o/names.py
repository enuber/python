# files are a way to save data persistently. 
# open - opens a file, opens it programatically so we can read it or write to it. 

# names = []

# # remember _ just means we are running the loop but not using any info or variables inside the loop. So could be named i but doesn't matter.

# for _ in range (3):
#   names.append(input("what's your name? "))

# for name in sorted(names):
#   print(f"Hello, {name}")

# name = input("what's your name? ")

# second argument tells it we will write to it. The first name of the file will be created if it doesn't already exist.
# "w" is for write
# open returns a file handle so we can access it. 
# if you repeat this, it will overwrite what was there. So have to be careful. Need to be appending to the file instead of overwriting
# "a" in this case is short for append, this though still puts the text all run together. It's appending back to back. We need to add a newline ourselves so it puts the names on it's own line.

# file = open("names.txt", "w")
# file = open("names.txt", "a")

# .write is a method that lets us write to the file and .close() closes the file.
# with - automatically open and then close the file. Along with this, the file name goes at the end of the line. So as <filename> is the file we want to be using.

# file.write(f"{name}\n")
# file.close()

# this opens and closes so you don't forget it as well.
# with open("names.txt", "a") as file:
#   file.write(f"{name}\n")

# to read an existing file...
# r - stands for read. 
# readlines is a special keyword that reads all the lines in the file and returns them as a list.

  # with open('names.txt', 'r') as file:
  #   lines = file.readlines()

  # for line in lines:
  #   # rstrip() here is just removing the \n that is in the file since print already gives us a new line already so there isn't a second newline
  #   print('Hello,', line.rstrip())

# this shortens the above simplifying the process as it's normal expected behaviour so python allows this.
  
# with open('names.txt', 'r') as file:
#   for line in file:
#     print('Hello,', line.rstrip())
  


# to sort the data before printing...

names = []

# r isn't required, just saying name of file will read the file. 
with open('names.txt') as file:
  for line in file:
    names.append(line.rstrip())

# allows you to reverse the order from Z-A, this is in the docs on sorted
for name in sorted(names, reverse=True):
  print(f"hello, {name}")

# can also be simplified
# with open('names.txt') as file:
#   for line in sorted(file):
#     print("hello,", line.rstrip())