import requests
from bs4 import BeautifulSoup
from random import randint
from metafinder.utils.exception import GoogleCaptcha, GoogleCookiePolicies
from metafinder.utils.agent import user_agent
import urllib3
urllib3.disable_warnings()


def search(target, total):
	documents = []
	start = 0
	num = 50 if total > 50 else total
	iterations = int(total/50)
	if (total%50) != 0:
		iterations += 1
	## Check https://github.com/n4xh4ck5/RastLeak - thanks Nacho
	url_base = f"https://www.google.com/search?q=(ext:pdf OR ext:doc OR ext:docx OR ext:xls OR ext:xlsx OR ext:ppt OR ext:pptx)+(site:*.{target} OR site:{target})&num={num}"
	cookies = {"CONSENT": "YES+srp.gws"}
	while (start < iterations) and (len(documents) < total):
		try:
			url = url_base + f"&start={start}"
			response = requests.get(url, 
			headers={'User-agent': 'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)'},
			timeout=5,
			verify=False,
			allow_redirects=False,
			cookies=cookies)
			text = response.text
			if response.status_code == 302 and ("htps://www.google.com/webhp" in text or "https://consent.google.com" in text):
				raise GoogleCookiePolicies()
			if "detected unusual traffic" in text:
				raise GoogleCaptcha()
			soup = BeautifulSoup(text, "html.parser")
			all_links = soup.find_all("a")
			follow = False
			for link in all_links:
				href = link.get("href", None)
				if href and target in href and "google" not in href:
					try:
						href = "http" + href.split("=http")[1]
						href = href.split("&sa=U&")[0]
						follow = True
						if href not in documents:
							documents.append(href)
							if len(documents) >= total:
								break
					except:
						continue
			if not follow:
				break
		except Exception as ex:
			raise ex #It's left over... but it stays there
		start += 1
	return documents	