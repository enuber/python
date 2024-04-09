import re

url = input("URL: ").strip()

# the removeprefix will remove this portion of the code if it exits at the beginning, else it doesn't do anything.
# username = url.removeprefix("https://twitter.com/")

# print(f"Username: {username}")


# re.sub(pattern, repl, string, count=0, flags=0)
# stands for substitute
# pattern - what to look for
# repl - what we want to replace it with
# string - what we want to do the subsitution on
# count - how many times do you want to do it. 
# flags - same as before

# s? is if s is there or not same with the (www\.)?
# this fails if someone enters like a google.com and doesn't do twitter at all

# username = re.sub(r'^(https?://)?(www\.)?twitter\.com', '', url)
# print(f"Username: {username}")

# going back to search instead. 
# ?: doesn't capture that area
# removed the $ at the end because we will tollerate things following user name but, we don't care about it.

if matches := re.search(r'^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)', url, re.IGNORECASE):
  print(f"Username:", matches.group(1))


# re.split(pattern, string, maxsplit=0, flags=0)
# allows you to split a string.

# re.findall(pattern, string, flags=0)
# allows you to search for a pattern in multiple places.