import os
import sys

from PIL import Image

#grab 1st and 2nd arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check is new/exists, if not create new
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

#loop through Pokedex
for filename in os.listdir(image_folder):
  img = Image.open(f'{image_folder}{filename}')
  clean_name = os.path.splitext(filename)[0]
  img.save(f'{output_folder}{clean_name}.png', 'png')
  print('all done')

#Convert images to png
#save to new folder
#first attempt to GitHub integration
