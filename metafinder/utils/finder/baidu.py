import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from metafinder.utils.exception import BaiduDetection
from metafinder.utils.agent import user_agent
import urllib3
urllib3.disable_warnings()


def search(target, total):
	documents = []
	base_url = "https://www.baidu.com/s?ie=utf-8"
	total_loop = int(total/10)
	if (total%10) != 0:
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
		new_url = base_url + f"&pn={count*10}&wd=(site:{target}+|+site:*.{target})+filetype:pdf"
		try:
			new_agent = user_agent.get(count, next_useragent)
			response = requests.get(new_url, headers=new_agent)
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
		for d in documents:
			resp = requests.get(d, allow_redirects=False)
			try:
				location = resp.headers.get("Location", None) # Get redirection (Real link)
				if location and location not in return_documents:
					return_documents.append(location)
			except:
				pass
	return return_documents	
