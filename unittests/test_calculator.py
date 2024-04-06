# testing the square function in calculator
# realize that the function below if the program works, won't actually do anything
# assert - keyword reduces the if and print statements making writing testing code easier.
# it is still bulky to do try/except as well.

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

  # run test by typing python filename.py
  # in the terminal it will show the tests that fail. in red and starts wth an E
  # if it passes, it will show passed in green and 100%
  
  assert square(2) == 4
  assert square(3) == 9
  assert square(-2) == 4
  assert square(-3) == 9
  assert square(0) == 0


def main():
  test_square()

if __name__ == "__main__":
  main()