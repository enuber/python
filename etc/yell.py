# comes after unpack
# map - purpose is to map something to every item in a sequence
# map(function, iterable, ...)

# def main():
#   yell("this", "is", "cs50")

# def yell(*words):
#   uppercased = []
#   for word in words:
#     uppercased.append(word.upper())
#   print(*uppercased)

# if __name__ == "__main__":
#   main()

# def main():
#   yell("this", "is", "cs50")

# def yell(*words):
#   # we don't use upper() because we don't want to call it now, we want to pass it to the map function to be used.
#   uppercased = map(str.upper, words)
#   print(*uppercased)

# if __name__ == "__main__":
#   main()


# list comprehensions - refers to create list on the fly rather than call append over and over.

def main():
  yell("this", "is", "cs50")

def yell(*words):
  uppercased = [word.upper() for word in words]
  print(*uppercased)

if __name__ == "__main__":
  main()