import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from metafinder.utils.exception import BaiduDetection
from metafinder.utils.agent import user_agent
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib3
urllib3.disable_warnings()

def _get_link(baidu_link):
	location = None
	try:
		resp = requests.get(baidu_link, timeout=5, allow_redirects=False)
		location = resp.headers.get("Location", None) # Get redirection (Real link)
	except:
		pass
	return location

def search(target, total):
	num_results = 50 if total >= 50 else total
	documents = []
	base_url = "https://www.baidu.com/s?ie=utf-8"
	total_loop = int(total/num_results)
	if (total%num_results) != 0:
		total_loop += 1
	count = 1
	old_useragent = -1
	total_timeout = 0
	while (count <= total_loop) and (len(documents) < total):
		while True:
			next_useragent = randint(0, len(user_agent)-1)
			if next_useragent != old_useragent:
				break
		old_useragent = next_useragent
		new_url = base_url + f"&pn={count*num_results}&wd=(site:{target}+|+site:*.{target})+filetype:pdf&rn={num_results}"
		try:
			new_agent = user_agent.get(count, next_useragent)
			response = requests.get(new_url, headers=new_agent, timeout=5, verify=False)
			text = response.text
			if "timeout-button" in text:
				total_timeout += 1
				if total_timeout == 5:
					raise BaiduDetection
				sleep(2)
				continue
			soup = BeautifulSoup(text, "html.parser")
			all_h3 = soup.findAll("h3", {"class": "t"})
			for h3 in all_h3:
				href = h3.a.get("href", None)
				if href and href not in documents:
					documents.append(href)
				if len(documents) >= total:
					break	
		except Exception as ex:
			raise ex #It's left over... but it stays there
		count += 1
	return_documents = []
	with ThreadPoolExecutor(max_workers=6) as executor:
		future_download = {executor.submit(_get_link, url): url for url in documents}
		for future in as_completed(future_download):
			try:
				data = future.result()
				if data and data not in return_documents:
					return_documents.append(data)
			except:
				pass
	return return_documents	
