# Packages are libraries that other people have built that have to be installed. It is generally in a folder not just a file. It is a third party library. pypi.org is where they are located. 
# to install packages python has it's own package manager called pip in our case pip3 since we are using python3

# import cowsay
# import sys

# if len(sys.argv) == 2:
#   cowsay.cow("hello, " + sys.argv[1])
  # cowsay.trex("hello, " + sys.argv[1])


# later lesson when we are using our own "library"
# need to use the __name__ in the other file so that it ignores the call to main and just runs what we need.

import sys
from sayings import hello

if len(sys.argv) == 2:
  hello(sys.argv[1])

