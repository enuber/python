# testing the square function in calculator
# realize that the function below if the program works, won't actually do anything
# assert - keyword reduces the if and print statements making writing testing code easier.
# it is still bulky to do try/except as well.
# good to have your work in functions rather than main so you can test them. The more bite sized the functions with explicit goals the easier to write tests for them.

import pytest
from calculator import square


# convention is to call the test function test__nameoffunction

def test_square():
  # if square(2) != 4:
  #   print('2 squared was not 4')
  # if square(3) != 9:
  #   print('3 squared was not 9')

  # this is what you could have to write out. 
  # try:
  #   assert square(2) == 4
  # except AssertionError:
  #   print('2 squared was not 4')
  # try:
  #   assert square(3) == 9
  # except AssertionError:
  #   print('3 squared was not 9')
  # try:
  #   assert square(-2) == 4
  # except AssertionError:
  #   print('-2 squared was not 4') 
  # try:
  #   assert square(-3) == 9
  # except AssertionError:
  #   print('-3 squared was not 9')  
  # try:
  #   assert square(0) == 0
  # except AssertionError:
  #   print('0 squared was not 0')   

  # pytest allows you to test code third party library its a bit simpler to do unit tests, pytest deals with all of the try/except prints. 
  # pip3 install pytest
  # docs.pytest.org

  # run test by typing pytest filename.py
  # in the terminal it will show the tests that fail. in red and starts wth an E
  # if it passes, it will show passed in green and 100%
  # issue with the below is as soon as one fails, it stops so you don't get the results of all of them. 
  # separating them into smaller groups is better
  
  assert square(2) == 4
  assert square(3) == 9
  assert square(-2) == 4
  assert square(-3) == 9
  assert square(0) == 0

def test_positive():
  assert square(2) == 4
  assert square(3) == 9

def test_negative():
  assert square(-2) == 4
  assert square(-3) == 9

def test_zero():
  assert square(0) == 0

# here we are expecting an error if a string gets passed in. Can put in an error that would be expected based on a specific type of error.
def test_str():
  with pytest.raises(TypeError):
    square('cat')
  

# note don't need main with pytest. Each function will be called regardless.
  
# def main():
#   # test_square()
#   test_positive()
#   test_negative()
#   test_zero()

# if __name__ == "__main__":
#   main()