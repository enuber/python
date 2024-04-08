from hello import hello

# this won't work because the hello function doesn't return a value. It is a side effect. So you can't test it in the same way as a function with a return function. 

# note we changed the hello file so that it returned enabling us to test.

def test_default():
  assert hello() == "hello, world"

def test_argument():
  # need to remember to keep tests simple because otherwise would need to test your test so to speak. This isn't bad but better to just do assertions.
  for name in ["Hermione", "Harry", "Ron"]:
    assert hello(name) == f"hello, {name}"