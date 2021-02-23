from os import sep, listdir, remove
import os.path
from concurrent.futures import ThreadPoolExecutor, as_completed
from metafinder.utils.file.metadata import extract_metadata
import time
from os import sep
import requests
from random import randint
from metafinder.utils.agent import user_agent

# Disable warning by SSL certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from metafinder.utils.color_print import print_error, print_ok


def download_document(url, directory, display):
	metadata = {}
	try:
		name = url.split(sep)[-1]
		file_name = directory + sep + name
		response = requests.get(url, headers=user_agent.get(randint(0, len(user_agent)-1)), timeout=5)
		s_code = response.status_code
		if s_code == 200:
			with open(file_name, "wb") as f:
				f.write(response.content)
			data = extract_metadata(file_name)
			if data:
				metadata = {
					"name": name, 
					"url": url, 
					"metadata": data}
			if display:
				print_ok(f"Downloaded file {url}")
		elif s_code == 404 and display:
			print_error(f"(404) File {url} Not Found")
		elif s_code == 403 and display:
			print_error(f"(403) Access to the file {url} is forbidden")
		elif display:
			print_error(f"({s_code} {url}")	
	except Exception as ex:
		if display:
			print_error(f"Error donwloading {url} >> {ex}")
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
			except Exception as ex:
				if display:
					print_error(f"Error: {ex}")
	try:
		for f in listdir(directory):
			remove(os.path.join(directory, f))
	except:
		pass
	return metadata_files

