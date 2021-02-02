from time import sleep
from os import system, sep
import wget
from metafinder.utils.file.metadata import extract_metadata

# Disable warning by SSL certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


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
				name = document.split(sep)[-1]
				metadata_files[name] = {}
				metadata_files[name]["url"] = url
				metadata_files[name]["files"] =  metadata
		sleep(2)
		system(f'rm {directory}/*')
		return metadata_files
	except Exception as ex:
		print(ex)
		return None
