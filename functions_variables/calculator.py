# second part of lecture 1

# ** raise to power of so 2 ** 3 would be 2 * 2 * 2
# can also do pow(n, 3) where n is the number to be raised to a power of and, the number after the comma is what power you are raising it too.

# when you do this, it becomes a string so this would join the numbers together even though it looks like it should be a number.

x = input('What\'s x? ')
y = input('What\'s y? ')

z = x+y
print(z)

# to fix the above

z = int(x) + int(y)
print(z)

# can further reduce this by getting rid of 'z'

a = int(input('What\'s x? '))
b = int(input('What\'s y? '))

print (a + b)

# float - number with a decimal point, 
# round - round(number[, ndigits]) from documentation, first argument is the number, the rest of this, [] means it is an optional parameter, in this case if we want to specify the number of digits to round to we can specify it here by using a comma and then adding in a number to round too

c = float(input('What\'s x? '))
d = float(input('What\'s y? '))

print (c + d)

z = round(c + d, 2) # will give decimal with 2 places

# this is saying that we will print z but, use a comma for large numbers
print(f"{z:,}")


# division - int can be as big as you want them to be, but the floating point value can only go so far. 

a = 4.543453452
b = 5.23424
 
c = a/b
print(c)

# way to specify with an f string how many digits you want to print. 

print(f"{c:.2f}") #will print up to two decimal places, different way to do this beyond using rounds functionality.