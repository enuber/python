def hello(name):
  print(f"hello, {name}")

def goodbye(name):
  print(f"goodbye, {name}")

def main():
  hello('world')
  goodbye('world')

# this vairable is a special variable automatically set by python to be name when you run a file from the command line.

if __name__ == "__main__":
  main()