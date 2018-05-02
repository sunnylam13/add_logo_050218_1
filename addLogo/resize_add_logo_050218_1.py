# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 resize_add_logo_050218_1.py

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
target_dir = '.' # use '.' for current working directory (cwd)
output_dir = 'withLogo'

logoIm = Image.open(LOGO_FILENAME)
logoWidth,logoHeight = logoIm.size # `logoIm.size` returns a tuple of width, height

os.makedirs(output_dir,exist_ok=True) # create a folder unless it already exists

# loop over all files in the working directory

for filename in os.listdir(target_dir):
	if not ( filename.endswith('.png') or filename.endswith('.jpg') or filename == LOGO_FILENAME ):
		continue # skip non-image files and the logo file itself

	im = Image.open(filename)
	width,height = im.size

# check if the image needs to be resized

if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
	# calculate the new width and height to resize to
	if width > height:
		height = int( (SQUARE_FIT_SIZE/width) * height )
		width = SQUARE_FIT_SIZE
	else:
		width = int( (SQUARE_FIT_SIZE/height) * width )
		height = SQUARE_FIT_SIZE

	# resize the image
	print('Resizing %s...' % str(filename))
	im = im.resize( (width,height) )

# add the logo
# save changes

