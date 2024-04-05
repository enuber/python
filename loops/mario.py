# based on other lessons
def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
  # for _ in range(height):
  #     print("#")
  # the below does the same thing, just a different way of doing it as previously seen
  print("#\n" * height, end="")

def print_row(width):
   print("?" * width)

# def print_square(size):
#    # for each row in square
#    for i in range(size):
#       # for each brick in row
#       for j in range(size):
#          # print brick
#          print("#", end="")
#       # this goes to a new line after the bricks are all printed at end of row
#       print()  

# simplified print_square
def print_square(size):
   for i in range(size):
      print("#" * size) 

main()