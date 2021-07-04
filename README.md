<h1 align="center">
  <b>MetaFinder</b>
  <br>
</h1>
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python"> 
  </a>
   <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
    <img src="https://img.shields.io/badge/license-GNU-green.svg?style=square&logo=gnu">
   <a href="https://twitter.com/JosueEncinar">
    <img src="https://img.shields.io/badge/author-@JosueEncinar-orange.svg?style=square&logo=twitter">
  </a>
</p>

<p align="center">
Search for documents in a domain through Search Engines. The objective is to extract metadata. 
</p>
<br/>

## Installation:

```
> pip3 install metafinder
```

Upgrades are also available using:

```
> pip3 install metafinder --upgrade
```

## Usage 

MetaFinder can be used in 2 ways:

### CLI
```
metafinder -d domain.com -l 20 -o folder [-t 10] -go -bi -ba
```

Parameters:
* d: Specifies the target domain.
* l: Specify the maximum number of results to be searched in the searchs engines.
* o: Specify the path to save the report.
* t: Optional. Used to configure the threads (4 by default).
* v: Show Metafinder version.
* Search Engines to select (Google by default):
  * go: Optional. Search in Google.
  * bi: Optional. Search in Bing.
  * ba: Optional. Search in Baidu. (Experimental)

### In Code
```
import metafinder.extractor as metadata_extractor

documents_limit = 5
domain = "target_domain"
result = metadata_extractor.extract_metadata_from_google_search(domain, documents_limit)
# result = metadata_extractor.extract_metadata_from_bing_search(domain, documents_limit)
# result = metadata_extractor.extract_metadata_from_baidu_search(domain, documents_limit)
authors = result.get_authors()
software = result.get_software()
for k,v in result.get_metadata().items():
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

## Example

![image](https://user-images.githubusercontent.com/16885065/118243158-69ee7600-b49e-11eb-9562-2dc1fab59d67.png)

# Author

This project has been developed by:

* **Josué Encinar García** -- [@JosueEncinar](https://twitter.com/JosueEncinar)


# Contributors


* **Félix Brezo Fernández** -- [@febrezo](https://twitter.com/febrezo)


# Disclaimer!

The software is designed to leave no trace in the documents we upload to a domain. The author is not responsible for any illegitimate use.
