
from setuptools import setup, find_packages
from os import path
import metafinder


long_description = """|Supported Python versions| |License|

**MetaFinder - Metadata search through Search Engines**
=======================================================

::

       _____               __             ___________ .__               .___                   
      /     \     ____   _/  |_  _____    \_   _____/ |__|   ____     __| _/   ____   _______  
     /  \ /  \  _/ __ \  \   __\ \__  \    |    __)   |  |  /    \   / __ |  _/ __ \  \_  __ \ 
    /    Y    \ \  ___/   |  |    / __ \_  |     \    |  | |   |  \ / /_/ |  \  ___/   |  | \/ 
    \____|__  /  \___  >  |__|   (____  /  \___  /    |__| |___|  / \____ |   \___  >  |__|    
            \/       \/               \/       \/               \/       \/       \/          
            
    |_ Author: @JosueEncinar
    |_ Description: Search for documents in a domain through Search Engines. The objective is to extract metadata
    |_ Usage: metafinder -d domain.com -l 50 -o /tmp -go -bi

Installation:
-------------

::

    > pip3 install metafinder

Upgrades are also available using:

::

    > pip3 install metafinder --upgrade

Usage
-----

CLI
~~~

::

    metafinder -d domain.com -l 20 -o folder [-t 10] -go -bi -ba 

Parameters: 

-  d: Specifies the target domain. 
-  l: Specify the maximum number of results to be searched. 
-  o: Specify the path to save the report. 
-  t: Optional. Used to configure the threads (4 by default). 
-  v: Show Metafinder version.
-  go: Optional. Search in Google. (Default) 
-  bi: Optional. Search in Bing. 
-  ba: Optional. Search in Baidu. (Experimental)

In Code
~~~~~~~

::

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

Author
======

This project has been developed by:

-  **Josué Encinar García** -- https://twitter.com/JosueEncinar

Contributors
============

-  **Félix Brezo Fernández** -- https://twitter.com/febrezo

Disclaimer!
===========

The software is designed to leave no trace in the documents we upload to a domain. The author is not responsible for any
illegitimate use.

.. |Supported Python versions| image:: https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python
.. |License| image:: https://img.shields.io/badge/license-GNU-green.svg?style=flat-square&logo=gnu

"""

setup(
    name='metafinder',
    version=metafinder.__version__,
    author='Josue Encinar (@JosueEncinar)',
    description='MetaFinder - Metadata search through Search Engines',
    include_package_data=True,
    license='GNU GPLv3+',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Josue87/MetaFinder",
    entry_points={
        'console_scripts': [
            'metafinder=metafinder.cli:main',
        ],
    },
    install_requires=[
        "requests>=2.25.1",
        "pikepdf>=2.5.2",
        "beautifulsoup4>=4.9.3",
        "openpyxl>=3.0.5",
        "python-docx>=0.8.6",
        "python-pptx>=0.6.18",
        "prompt-toolkit>=3.0.5",
        "urllib3>=1.26.4"
    ]
)
