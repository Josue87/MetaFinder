from os import mkdir
from os.path import exists


def new_directory(directory):
	try:
		if not exists(directory):
			mkdir(directory)
	except Exception as ex:
		print(ex)
