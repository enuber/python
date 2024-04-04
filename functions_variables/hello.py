# in terminal can type in python3 and get >>> which becomes interactive mode and you can write code directly into the terminal then and get immediate responses without having to run the whole program.

# code hello.py in terminal will create the file and/or open it
# python plus file name will run the program
# move file from folder to parent use mv filename ..
# to run from some windows you may have to python hello.py which will pass the file to the interperter from top to bottom, left to right

#function is an action or verb that lets you do some things. There are some functions that come already built in, in this case print() is a function that will print what you want it to. An arguement is what is passed into the function. A side effect is the result of running that function. in print() the side effect is to print what's placed in it.

#input() lets you get input from a user. you can then store that into a variable and use it later.

#variables - let you store data in them to be called later, should be called something that makes sense to what it is storing

# comments for multi-lines can be done with triple quotes or just using the # on each line

"""
this is a comment
"""

# to add to a line, you can use the + sign but, you can also use a comma, in this case the comma adds in a space. When you pass multiple arguments to print with a comma list, it automatically adds a space between. The plus sign in this case is concatenation. It is not considered addition in this case.

#type of data 
# str - string

#print function offical doc
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=false)
# how to read this. What is between the () are the parameters that can be passed in. When you use the function and send the parameters in, the parameters are called the arguements so the words mean the same thing. In the case of print() they are called positional parameters because based on where they are located in the function the first things is printed first, the second is second and so on. sep="" and end="" are named parameters.
# *objects mean that we can pass in as many objects as you want, sep is short for separator, and the the end='\n' means that there is a new line. So every time we use print() we get a new line. 
# by breaking this down, sep=' ' means when we use the comma as a seperator, we get a space. so this can be replaced with anything and, with the end we could replace with something else.

# for printing quotes inside a string, you can either do the opposite type of quote as the wrapper, like single quote on outside for double quote on inside or vice versa else you use an escape character which is the backslash \




name = input("What's your name? ")

print("hello " + name)
print("hello,", name)

# overriding the end= newline and replace it with nothing will mean this stays all on one line. You can put anyting in end but know that it will tack onto the end of the print function before doing the next line of code. This would go for sep as well. 
print("hello ", end="")
print(name) # hello <name>
print("hello ", end='???')
print(name) # hello ???<name>


# for longer strings there is another way you can use f before the string and then wrap the variables in {} braces. 

print(f"hello, {name}")

# can clean up text, there are built in features to string.

name = name.strip() # removes whitespace from str, this is done right to the left so name will be stripped of white spaces and assigned back to name. lstrip() and rstrip() will strip from one direction or the other as well.

name = name.capitalize() # capitalizes the first letter so if there were multiple names it would only do the first letter of the first word

name = name.title() # capitalizes each word

#these can be chained together so can do

name = name.strip().title() 

# even more we can add this back onto the input to make even less code

name = input("what's your name? ").strip().title()

# split() will split words this will place the first word into first and second word into last. This will be split by the empty space, so what is between the split() will be what will make something split.
first, last = name.split(' ');

# numbers
# +, -, *, /, % 
# percent sign is the modulo which is the remainder after dividng one number by the other

