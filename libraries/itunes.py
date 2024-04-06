#API - can get to an API with requests which is the keyword
# pypi.org/project/requests
# JSON - can be read by python. and acessed. 
# use .json() to show the response as json on screen
# in this case we get it back as a python dictionary. it is a json response but python request library makes it a dictionary.
# there is a json library that helps clean up this code so its easier to see and understand. comes with python it's called json. 

import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# this is how we use the json clean up so we see it as a list. 
# print(json.dumps(response.json(), indent=2))

obj = response.json()

for result in obj['results']:
  print(result['trackName'])

