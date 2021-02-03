![Supported Python versions](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square&logo=gnu)

# **MetaFinder - Metadata search through Google**

```
   _____               __             ___________ .__               .___                   
  /     \     ____   _/  |_  _____    \_   _____/ |__|   ____     __| _/   ____   _______  
 /  \ /  \  _/ __ \  \   __\ \__  \    |    __)   |  |  /    \   / __ |  _/ __ \  \_  __ \ 
/    Y    \ \  ___/   |  |    / __ \_  |     \    |  | |   |  \ / /_/ |  \  ___/   |  | \/ 
\____|__  /  \___  >  |__|   (____  /  \___  /    |__| |___|  / \____ |   \___  >  |__|    
        \/       \/               \/       \/               \/       \/       \/          
        
|_ Author: @JosueEncinar
|_ Description: Search for documents in a domain through Google. The objective is to extract metadata
|_ Usage: python3 metafinder.py -t domain.com -l 100

```

## Installing dependencies:

```
> pip3 install metafinder
```

Upgrades are also available using:

```
> pip3 install metafinder --upgrade
```

## Usage 

```
metafinder -t domain.com -l 20 -o folder [-v] 
```

Parameters:
* t: Specifies the target domain.
* l: Specify the maximum number of results to be searched.
* o: Specify the path to save the report.
* v: Optional. It is used to display the results on the screen as well.

# Author

This project has been developed by:

* **Josué Encinar García** -- [@JosueEncinar](https://twitter.com/JosueEncinar)


# Contributors


* **Félix Brezo Fernández** -- [@febrezo](https://twitter.com/febrezo)


# Disclaimer!

This Software has been developed for teaching purposes and for use with permission of a potential target. The author is not responsible for any illegitimate use.
