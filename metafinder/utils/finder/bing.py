from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from random import randint
from metafinder.utils.agent import user_agent

def search(target, total):
	bing_count = 25
	documents = []
	url = f"https://www.bing.com/search?q=site:{target}+(filetype:pdf+OR+filetype:doc+OR%20filetype:docx+OR+filetype:xls+OR+filetype:xlsx+OR+filetype:ppt+OR+filetype:pptx)&count={bing_count}"
	try:
		count = 0
		iter_count = int(total/bing_count)
		if (total%bing_count) != 0:
			iter_count +=1
		while (count < iter_count) and (len(documents) < total):
			this_count = count*bing_count + 1
			new_url = url + f"&first={this_count}&FORM=PERE"
			req = Request(new_url, headers={"User-Agent": user_agent.get(randint(0, len(user_agent)-1))["User-agent"]})
			page = urlopen(req)
			soup = BeautifulSoup(page.read(), "html.parser")
			all_links = soup.find_all("a")
			for link in all_links:
				href = link.get("href", None)
				if href and target in href and \
				(href.endswith("pdf") or href.endswith("doc") or href.endswith("docx") or href.endswith("ppt") or href.endswith("pptx") or href.endswith("xls") or href.endswith("xlsx")) \
				and href not in documents:
					documents.append(href)
					if len(documents) >= total:
						break
			count += 1
	except Exception as e:
		pass
	return documents	
