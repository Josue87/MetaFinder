from os import sep, listdir, remove
import os.path
from concurrent.futures import ThreadPoolExecutor, as_completed
from metafinder.utils.file.metadata import extract_metadata
import time
from os import sep
import requests
from random import randint
from metafinder.utils.agent import user_agent
from metafinder.utils.var_data import * 

# Disable warning by SSL certificate
import urllib3
urllib3.disable_warnings()
from metafinder.utils.color_print import print_error, print_ok


def download_document(element, directory, display):
	metadata = {}
	url = element[CONST_URL]
	search_engines = element[CONST_SEARCH_ENGINES]
	try:
		name = url.split(sep)[-1]
		file_name = directory + sep + name
		response = requests.get(url, headers=user_agent.get(randint(0, len(user_agent)-1)), timeout=10, verify=False)
		s_code = response.status_code
		data = {}
		if s_code == 200:
			with open(file_name, "wb") as f:
				f.write(response.content)
			data = extract_metadata(file_name)
			if display:
				print_ok(f"Downloaded file {url}")
		elif display:
			print_error(f"(Status code: {s_code}) File {url}")
		metadata = {
			CONST_NAME: name, 
			CONST_URL: url, 
			CONST_METADATA: data,
			CONST_STATUS_CODE: s_code,
			CONST_SEARCH_ENGINES: search_engines}
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
					name = data[CONST_NAME]
					del data[CONST_NAME]
					metadata_files[name] = data
			except Exception as ex:
				if display:
					print_error(f"Error: {ex}")
	try:
		for f in listdir(directory):
			remove(os.path.join(directory, f))
	except:
		pass
	return metadata_files

