import requests
from urllib.parse import unquote
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#Disable warning by SSL certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup


def search(target, total):
	documents = []
	user_agent = {'User-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.86 Mobile Safari/537.36'}
	url = f"https://www.google.com/search?q=(ext:pdf OR ext:doc OR ext:docx OR ext:xls OR ext:xlsx OR ext:ppt)+(site:{target}+OR+site:*.{target}&filter=0&num={total}"
	try:
		response = requests.get(url, headers=user_agent)
		text = response.text
		soup = BeautifulSoup(text, "html.parser")
		if text.find("detected unusual traffic") != -1:
			print("Captcha...")
			return documents
		all_links = soup.find_all("a")
		for link in all_links:
			href = link.get("href", None)
			if href and target in href:
				if href.endswith("pdf") or href.endswith("doc") or href.endswith("docx") or href.endswith("ppt") or href.endswith("xls"):
				    documents.append(href)
	except Exception as ex:
		print(ex)
	return documents	