# in order to run tests from a folder, you need to add a special file to the folder. file is called __init__.py and, even if nothing is in it, it tells python to treat that folder not just as module but a package. 

# then you can test everything inside that folder by just typing pytest test where test is the name of the folder. can do this from outside the test folder.

from hello import hello

def test_default():
  assert hello() == "hello, world"

def test_argument():
  assert hello("David") == 'hello, David'