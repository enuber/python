# generators - can generator a massive amount of data but only return a little at time. 
# yield - tells python to return one value at a time from a loop.
# iterator - is what is returned from the yield. it allows yield to step over it one at a time and keeps track of where it is at. 

# def main():
#   n = int(input("What's n? "))
#   for i in range(n):
#     print(sheep(i))

# def sheep(n):
#   return "sheep " * n

# if __name__ == "__main__":
#   main()

# if we try to do this for a large amount the comptuer will start to struggle. 

# def main():
#   n = int(input("What's n? "))
#   for s in sheep(n):
#     print(s)

# def sheep(n):
#   flock = []
#   for i in range(n):
#     flock.append("sheep " * i)
#   return flock  

# if __name__ == "__main__":
#   main()


# because of yield, this now works because it's doing one line at a time rather than trying to do it all at once and taking to long, or just burning out.

def main():
  n = int(input("What's n? "))
  for s in sheep(n):
    print(s)

def sheep(n):
  for i in range(n):
    yield "sheep " * i

if __name__ == "__main__":
  main()
