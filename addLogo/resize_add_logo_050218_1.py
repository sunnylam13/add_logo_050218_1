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
target_dir = '.' # use '.' for current working directory (cwd), default target folder
target_dir = "/Users/sunnyair/Dropbox/Python Programming/auto_bore_py_020518_1"
output_dir = 'withLogo' # default output folder
output_dir = "/Users/sunnyair/Downloads/withLogo"

logoIm = Image.open(LOGO_FILENAME)
logoWidth,logoHeight = logoIm.size # `logoIm.size` returns a tuple of width, height

os.makedirs(output_dir,exist_ok=True) # create a folder unless it already exists

# change current working directory if not using the default

if target_dir != ".":
	os.chdir(target_dir)

# loop over all files in the working directory

# logging.debug( 'Files in target directory are:  %s' % str( os.listdir(target_dir) ) )

for filename in os.listdir(target_dir):

	if not ( filename.endswith('.png') or filename.endswith('.jpg') or filename == LOGO_FILENAME ):
		continue # skip non-image files and the logo file itself, i.e. skip remaining code below if it does not match our conditions

	logging.debug( 'Accessing file:  %s' % str(filename) )

	logging.debug( 'Opening file:  %s' % str(filename) )
	im = Image.open(filename)
	logging.debug( 'Opening file successful:  %s' % str(filename) )
	width,height = im.size
	logging.debug( 'Width and height of image are:  W %d , H %d' % (width,height) )

	# check if the image needs to be resized

	if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
		logging.debug( 'Image exceeds our fit size' )
		# calculate the new width and height to resize to
		if width > height:
			logging.debug( 'Width is greater than height.' )
			height = int( (SQUARE_FIT_SIZE/width) * height )
			width = SQUARE_FIT_SIZE
		else:
			logging.debug( 'Height is greater than width.' )
			width = int( (SQUARE_FIT_SIZE/height) * width )
			height = SQUARE_FIT_SIZE

		# resize the image
		print('Resizing %s...' % str(filename))
		im = im.resize( (width,height) )
		logging.debug( 'Resizing image successful.' )

	# add the logo
	print("Adding logo to %s..." % str(filename) )
	im.paste( logoIm, (width - logoWidth, height - logoHeight), logoIm ) # passing 3rd arg pastes transparency pixels as well

	# save changes
	im.save( os.path.join(output_dir,filename) )

