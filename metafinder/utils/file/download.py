from os import sep, listdir, remove
import os.path
import wget
from concurrent.futures import ThreadPoolExecutor, as_completed
from metafinder.utils.file.metadata import extract_metadata

# Disable warning by SSL certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_document(url, directory, display):
	metadata = {}
	try:
		if display:
			print(f"[+] Downloading {url}")
		document = wget.download(url, directory, bar=None)
		data = extract_metadata(document)
		if data:
			name = document.split(sep)[-1]
			metadata = {
				"name": name, 
				"url": url, 
				"metadata": data}
	except Exception as ex:
		if display:
			print(f"[-] Error ({url}): {ex}")
	return metadata


def download_file(urls_metadata, directory, threads, display=True):
	metadata_files = {}

	with ThreadPoolExecutor(max_workers=threads) as executor:
		future_download = {executor.submit(download_document, url, directory, display): url for url in urls_metadata}
		for future in as_completed(future_download):
			try:
				data = future.result()
				if data:
					name = data["name"]
					metadata_files[name] = {}
					metadata_files[name]["url"] = data["url"]
					metadata_files[name]["metadata"] =  data["metadata"]
			except Exception as exc:
				print(f"Error: {exc}")
	try:
		for f in listdir(directory):
			remove(os.path.join(directory, f))
	except:
		pass
	return metadata_files

