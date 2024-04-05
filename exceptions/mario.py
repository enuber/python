def main():
  height = int(input("height: "))
  pyramid(height)

# ways to debug, could print(i) to see what i is, this would show you that because of range, we are starting at 0 so even though we are asking for a height of say 3 we are getting two visible lines. So adding n+1 fixes this.
  
# breakpoints - allow you to pause code at a specific spot, allows you to stop it and continue it. In python, within vs code, if you click on the line number itself, it will show a red dot to create that breakpoint.

# on left side choose the debugger and run it. can then use the tools to walk through the code.

def pyramid(n):
  for i in range(n):
    print("#" * (i + 1))

if __name__ == '__main__':
    main()