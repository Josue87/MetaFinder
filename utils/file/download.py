from time import sleep
from os import system, sep
import wget
from utils.file.metadata import extract_metadata


def download_file(urls_metadata, target, directory):
	metadata_files = {}
	try:
		for url in urls_metadata:
			try:
				print(f"[+] Downloading {url}")
				document = wget.download(url, directory, bar=None)
			except Exception as ex:
				print(f"[-] Error: {ex}")
				continue
			metadata = extract_metadata(document)
			if metadata:
				metadata_files[document.split(sep)[-1]] =  metadata
		sleep(2)
		system(f'rm {directory}/*')
		return metadata_files
	except Exception as ex:
		print("FAILED")
		print(ex)
		return None