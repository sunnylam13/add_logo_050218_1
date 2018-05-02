try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This program adds a small logo watermark to multiple resized images.  It is a relatively inexpensive time saver compared to using expensive graphics programs.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Add Logo to Multiple Images'
}

setup(**config)