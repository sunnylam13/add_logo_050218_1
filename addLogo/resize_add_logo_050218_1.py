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

logoIm = Image.open(LOGO_FILENAME)
logoWidth,logoHeight = logoIm.size # `logoIm.size` returns a tuple of width, height

# loop over all files in the working directory
# check if the image needs to be resized
# calculate the new width and height to resize to
# resize the image
# add the logo
# save changes


