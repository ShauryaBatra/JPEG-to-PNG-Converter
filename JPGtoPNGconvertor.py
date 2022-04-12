import sys
import os
from PIL import Image
 
# Grab first and second argument

image_folder = sys.argv[1]   #JPGtoPNGconvertor.py has index 0, pokedex, 1 and   
output_folder = sys.argv[2]  #New, 2, if New exists or is created later

print(image_folder)
print(output_folder)


# check if new\ exists, if not create it.

if not (os.path.exists(output_folder)):  #.exists and .makedirs are methodes of the os module
	os.makedirs(output_folder)            #used to check wether a directory exists or to create a new directory
print(os.path.exists(sys.argv[2]))       #prints True or False depending upon wether the argument is present in the path  


# loop through pokedex

for filename in os.listdir(image_folder):
 img = Image.open(f'{image_folder}{filename}')


# convert images to png

 clean_image = os.path.splitext(filename)[0] 


# save to the new folder

 img.save(f'{output_folder}{clean_image}.png','png')



