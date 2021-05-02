# Contributing to Metafinder

## Contribution Steps

1. Send a Pull Request following our pull requests guidelines.
2. New PRs go to the master branch when merging.
3. In the PR, describe all the changes, issues and fixes.

## Building Metafinder

### Pre-requisites

- Python 3.8
- Pip

```
git clone https://github.com/Josue87/MetaFinder
cd metafinder
```

Create a new venv and install the dependencies:

```
python3 -m venv venv  
source venv/bin/activate
pip3 install -r requirements.txt
```

To start locally run 

```
python -m metafinder.cli [arguments]
```

