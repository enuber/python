import re

email = input("What's your email? ").strip()

# super basic and very bad to do
# if "@" in email and '.' in email:
#   print('Valid')
# else:
#   print('Invalid')

# username, domain = email.split('@')

# if username has at least one character it is considered valid
# being specific to just edu emails
# again this is bad 


# if username and domain.endswith('.edu'):
#   print('valid')
# else:
#   print('invalid')

# re is a library for regular expressions
# re.search(pattern, string, flags=0)

# same as above, still very bad. but starting out.
# if re.search('@', email):
#   print('valid')
# else:
#   print('invalid')

# regex special characters for building patterns
# . - any character except a newline
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetition
# {m} - m repetitions
# {m, n} - m-n repetitions
# ^ - matches the start of the string
# $ - matches the end of the string or just before the newlinte at the end of the string
# [] - set of characters like litterally typing them out as an ex [abcdef]
# [^] - complementing the set, the ^ here means basically not like [^abcdef] would be not any of those letters but everything else is okay.

# ..* would also work because we expect a character plus possibly more characters
# if re.search('.+@.+', email):
#   print('valid')
# else:
#   print('invalid')

# to get more specific can add in an end to email address can add it in and escape the period so it isn't the same as the . above where we expect a character. 
# need to include the r first so we are telling python to not interpret backslashes in the usual way. so here we are litterally asking to check that .edu is in the address.

# if re.search(r".+@.+\.edu", email):
#   print('valid')
# else:
#   print('invalid')  


# [^@] - every character but for the @ sign is allowed
# this will keep an email addres from having @@@ in it.

# if re.search(r"^[^@]+[@][^@]+\.edu$", email):
#   print('valid')
# else:
#   print('invalid') 

# [a-zA-Z] specifies that the address contains either lower or uppercase letters
# [a-zA-Z0-9_] - including now numbers and the underscore. This is a set, just says this is what can be typed here and validated, only these characters.

# if re.search(r"^[a-zA-Z0-9_]+[@][a-zA-Z0-9_]+\.edu$", email):
#   print('valid')
# else:
#   print('invalid') 

# \w - a word with the same meaning as the [a-zA-Z0-9_] expression
# \W - not a word character
# \d - decimal digit
# \D - not a decimal digit
# \s - whitespace characters
# \S - not a whitespace character
# A|B - either A or B
# (...) - a group ex (com|edu|gov|org)
# (?:...) - non-capturing version

# add in a space can litterally put a space in [a-zA-Z0-9_ ] or (\w|\s)
# note that the below will still fail .EDU since we are asking for .edu

# if re.search(r"^\w+[@]\w+\.edu$", email):
#   print('valid')
# else:
#   print('invalid')


# can use flags in re.search to set IGNORECASE, MULTILINE, DOTALL
# if you don't care about the case this would work to just ignore the cases entered
# (\w+\.)? - the question mark says this can be here or it may not but we want a word with at least one character and we expect a literal period. Could use * instead of ? so it would be one or more instead of 0 or 1

if re.search(r"^\w+[@](\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print('valid')
else:
  print('invalid')


# re.match(pattern, string, flag=0)
# re.match - doesn't have to start with ^ it will already start matching at begining of string
# re.fullmatch(pattern, string, flag=0)
# re.fullmatch - will match beginning and end of string so don't have to include ^ or $