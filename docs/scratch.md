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

