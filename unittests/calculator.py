# testing is about trying different types of data to see how the function responds to see if you can find any unexpected errors.

def main():
  x = int(input("what's x? "))
  print("x squared is", square(x))

def square(n):
  return n * n

if __name__ == "__main__":
  main()