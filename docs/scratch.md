# Scratch Notes and Log

## Wednesday, May 2, 2018 10:24 AM

High level

* load logo image

* loop over all `.png` and `.jpg` files in cwd

* check whether image is wide or taller than 300 px

* if it is, reduce width or height (whichever is large) to 640 pixels and scale down other dimension proportionally

* paste logo image in corner

* save the altered images to another folder

Code

* open the `catlogo.png` as `Image` object

* loop over strings returned from `os.listdir('.')`

* get the width and height of image from the `size` attribute

* calculate the new width and height of the resized image

* call the `resize()` method to resize the image

* call `paste()` to paste logo

* call `save()` method to save changes using original filename

## Wednesday, May 2, 2018 10:34 AM

adding:

	SQUARE_FIT_SIZE = 300
	LOGO_FILENAME = 'catlogo.png'

makes it easier to change later

	if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
		# calculate the new width and height to resize to
		if width > height:
			height = int( (SQUARE_FIT_SIZE/width) * height )
			width = SQUARE_FIT_SIZE
		else:
			width = int( (SQUARE_FIT_SIZE/height) * width )
			height = SQUARE_FIT_SIZE

you need to find out if the image is a wide or tall image if it does need to be resized...

## Wednesday, May 2, 2018 11:06 AM

want to add logo to the bottom right corner

## Wednesday, May 2, 2018 11:11 AM

Ideas for Similar Programs

* add text or a website URL to images

* add time stamps to images

* copy or move images into different folders based on their sizes

* add a mostly transparent watermark to an image to prevent others from copying it

## Wednesday, May 2, 2018 11:50 AM

for some reason `catlogo.png` is too large...  and doesn't fit in the bottom right corner...

## Monday, May 7, 2018 5:21 PM

Image File Extension Check

case insensitive

https://regexr.com/3p39j

## Tuesday, May 8, 2018 11:07 AM

I went with this IF statement:

	if not ( filename.endswith('.png') or filename.endswith('.jpg' or filename.endswith('.JPG') or filename.endswith('.PNG') or filename.endswith('.bmp') or filename.endswith('.BMP') or filename.endswith('.gif') or filename.endswith('.GIF') ) or filename == LOGO_FILENAME ):
		continue # skip non-image files and the logo file itself, i.e. skip remaining code below if it does not match our conditions

it was easier then having to use a regex search 

