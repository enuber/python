#command line arguments - allows you to provide arguments in command line when you are running the program. 

# docs.python.org/3/library/sys.html

#sys.argv - argument vector. list of all the words types in before they hit enter

import sys

# note: need to actually type in versus just hit the play button. 
# in sys.argv[0] is the name of the program. so the name of the file is in zero
# in our case argv[1] then stores the next thing typed in which is the name we gave it.
# if we don't type anything in, we get an IndexError: list index out of range
# can use " " around the name to add a full name 

# try:
#   print("hello, my name is", sys.argv[1])
# except IndexError:
#   print("too few arguments")

# if len(sys.argv) < 2:
#   print("too few arguments")
# elif len(sys.argv) > 2:
#   print("too many arguments")
# else:
#   print('hello, my name is', sys.argv[1])


# what we would like to do is separate checking for errors and then do the rest later
# we use sys.exit to end the program. So by the final print line, we know that are safe to proceed. It takes the string in and prints it out before exiting/ending the program.

# if len(sys.argv) < 2:
#   sys.exit("too few arguments")
# elif len(sys.argv) > 2:
#   sys.exit("too many arguments")

# print('hello, my name is', sys.argv[1])

# now want to itterate over a list of names typed in this prints out [0] though to which has the file name in it. So we need to take a slice of the list.
# to slice you use [whereyouwanttobe:] so can start where you want, then add a colon and it will start at that point and go to end of list.
# sequence[start:end:step] start: The index where the slicing starts. If omitted, slicing starts from the beginning of the sequence. If negative, it indicates an index relative to the end of the sequence. end: The index where the slicing ends (but doesn't include the element at this index). If omitted, slicing continues until the end of the sequence. If negative, it indicates an index relative to the end of the sequence. step: Optional. The step size for selecting elements. If omitted, the default step size is 1.

if len(sys.argv) < 2:
  sys.exit("too few arguments")

# will start at 1 and continue through
for arg in sys.argv[1:]:
  print('hello, my name is', arg)
