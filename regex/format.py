import re

name = input("What's your name? ").strip()

# if "," in name: 
#   last, first = name.split(', ')
#   name = f"{first} {last}"

# print(f"Hello, {name}")


# A|B - either A or B
# (...) - a group ex (com|edu|gov|org) - this captures whats in the () and returns it
# (?:...) - non-capturing version

# here we are capturing two words where they have any character one or more times before the comma and the same after the comma space
# matches = re.search(r"^(.+), ?(.+)$", name)

# if matches: 
#   # .groups() returns all the groups that were captured.
#   # last, first = matches.groups()
#   # name = f"{first} {last}"

#   # same as above but one line and notice group is 1 and 2 not zero based
#   name = matches.group(2) + " " + matches.group(1)
  
# print(f"hello, {name}")


# new to pythong the walrus operator := allows you to run an if statement and get assign something from right to left. Tightened up the code slightly.

if matches := re.search(r"^(.+), ?(.+)$", name):
  name = matches.group(2) + " " + matches.group(1)
  
print(f"hello, {name}")