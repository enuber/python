# global - variable outside of all functions. 
# UnboundLocalError - when you are in a function you can read a global variable but you can't write to it, ie change it from within a function
# global - is a keyword that informs a function that it is a globabl variable. need to declare it within functions.

# balance = 0

# def deposit(n):
#   global balance
#   balance += n

# def withdraw(n):
#   global balance
#   balance -= n

# def main():
#   print("Balance:", balance)
#   deposit(100)
#   withdraw(50)
#   print("Balance:", balance)

# if __name__ == "__main__":
#   main()

class Account:
  def __init__(self):
    # doing this to just note that it is private even though not enforced.
    self._balance = 0

  # this is a getter, there is no setter so you can't set the variable but you can get the value. This means you can't do account.balance = 1000 to give yourself 1000 so it prevents this type of usage and thus we have more control. We can just get the balance.
  @property
  def balance(self):
    return self._balance
  
  def deposit(self, n):
    self._balance += n
  
  def withdraw(self, n):
    self._balance -= n

def main():
  account = Account()
  print("Balance:", account.balance)
  account.deposit(100)
  account.withdraw(50)
  print("Balance:", account.balance)

if __name__ == "__main__":
  main()

  