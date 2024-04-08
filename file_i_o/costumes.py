# Pillow library is PIL

import sys

from PIL import Image

images = []

# this will open the images and open them up.
# rember that [1:] will take a slice and give us everything after 1 to the end.

for arg in sys.argv[1:]:
  image = Image.open(arg)
  images.append(image)

# the PIL library takes care of everything, does opening, closing and saving by just calling save.
# name of file to save is first,
# append images will allow you to append more files than just one as it's a list
# duration is time between frames
# loop=0 means infinite.
  
images[0].save(
  "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)