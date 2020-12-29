from os import mkdir
from os.path import exists


def new_directory(directory):
	try:
		if not exists(directory):
			print(f"[+] Creating  {directory} directory\n")
			mkdir(directory)
		else:
			print(f"[!] The {directory} directory already exists. Skipping mkdir\n")
	except Exception as ex:
		print(ex)
