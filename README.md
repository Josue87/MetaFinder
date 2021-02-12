![Supported Python versions](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square&logo=gnu)

# **MetaFinder - Metadata search through Search Engines**

```
   _____               __             ___________ .__               .___                   
  /     \     ____   _/  |_  _____    \_   _____/ |__|   ____     __| _/   ____   _______  
 /  \ /  \  _/ __ \  \   __\ \__  \    |    __)   |  |  /    \   / __ |  _/ __ \  \_  __ \ 
/    Y    \ \  ___/   |  |    / __ \_  |     \    |  | |   |  \ / /_/ |  \  ___/   |  | \/ 
\____|__  /  \___  >  |__|   (____  /  \___  /    |__| |___|  / \____ |   \___  >  |__|    
        \/       \/               \/       \/               \/       \/       \/          
        
|_ Author: @JosueEncinar
|_ Description: Search for documents in a domain through Search Engines. The objective is to extract metadata
|_ Usage: metafinder -d domain.com -l 50 -o /tmp -go -bi

```

## Installation:

```
> pip3 install metafinder
```

Upgrades are also available using:

```
> pip3 install metafinder --upgrade
```

## Usage 

### CLI
```
metafinder -d domain.com -l 20 -o folder [-t 10] [-v] -go
```

Parameters:
* d: Specifies the target domain.
* l: Specify the maximum number of results to be searched in the searchs engines.
* o: Specify the path to save the report.
* t: Optional. Used to configure the threads (4 by default).
* v: Optional. It is used to display the results on the screen as well.
* Search Engines to select (Google by default):
  * go: Optional. Search in Google.
  * bi: Optional. Search in Bing.
  * ba: Optional. Search in Baidu.

### In Code
```
import metafinder.extractor as metadata_extractor

documents_limit = 5
domain = "target_domain"
data = metadata_extractor.extract_metadata_from_google_search(domain, documents_limit)
# data = metadata_extractor.extract_metadata_from_bing_search(domain, documents_limit)
# data = metadata_extractor.extract_metadata_from_baidu_search(domain, documents_limit)
for k,v in data.items():
    print(f"{k}:")
    print(f"|_ URL: {v['url']}")
    for metadata,value in v['metadata'].items():
        print(f"|__ {metadata}: {value}")

document_name = "test.pdf"
try:
    metadata_file = metadata_extractor.extract_metadata_from_document(document_name)
    for k,v in metadata_file.items():
        print(f"{k}: {v}")
except FileNotFoundError:
    print("File not found")
```
# Author

This project has been developed by:

* **Josué Encinar García** -- [@JosueEncinar](https://twitter.com/JosueEncinar)


# Contributors


* **Félix Brezo Fernández** -- [@febrezo](https://twitter.com/febrezo)


# Disclaimer!

The software is designed to leave no trace in the documents we upload to a domain. The author is not responsible for any illegitimate use.
