from pathlib import Path
import tempfile
from os.path import isfile
from metafinder.utils.finder import google
from metafinder.utils.finder import bing
from metafinder.utils.finder import baidu
from metafinder.utils.file.download import download_file
from metafinder.utils.file.metadata import extract_metadata
from metafinder.utils.result import Result
from metafinder.utils.var_data import * 


def _generate_list(links, search_engine):
    result = []
    for link in links:
        result.append({
            CONST_URL: link,
            CONST_SEARCH_ENGINES: [search_engine]
        })
    return result

def extract_metadata_from_google_search(domain, limit=50, threads=4):
    """Search metadata in files through Google

    Args:
       domain: Target domain.
       limit: Maximum number of files to search.
       threads: Threads for downloading documents.
    
    Raises:
        GoogleCaptcha: If Google displays the captcha.
        Exception: If there is an error

    Returns:
        dict: Result object
    """
    links = google.search(domain, limit)
    directory = tempfile.TemporaryDirectory()
    metadata_files = None
    if links and len(links) > 0:
        metadata_files = download_file(_generate_list(links, "Google"), directory.name, threads, False)
    directory.cleanup()
    return Result(metadata_files) if metadata_files else None

def extract_metadata_from_bing_search(domain, limit=50, threads=4):
    """Search metadata in files through Bing

    Args:
       domain: Target domain.
       limit: Maximum number of files to search.
       threads: Threads for downloading documents.
    
    Raises:
        Exception: If there is an error

    Returns:
        dict: Result object
    """
    links = bing.search(domain, limit)
    directory = tempfile.TemporaryDirectory()
    metadata_files = None
    if len(links) > 0:
        metadata_files = download_file(_generate_list(links, "Bing"), directory.name, threads, False)
    directory.cleanup()
    return Result(metadata_files) if metadata_files else None

def extract_metadata_from_baidu_search(domain, limit=50, threads=2):
    """Search metadata in PDF files through Baidu (slow method)

    Args:
       domain: Target domain.
       limit: Maximum number of files to search.
       threads: Threads for downloading documents.
    
    Raises:
        BaiduDetection: If Google displays the captcha.
        Exception: If there is an error

    Returns:
        dict: Result object
    """
    links = baidu.search(domain, limit)
    directory = tempfile.TemporaryDirectory()
    metadata_files = None
    if len(links) > 0:
        metadata_files = download_file(_generate_list(links, "Baidu"), directory.name, threads, False)
    directory.cleanup()
    return Result(metadata_files) if metadata_files else None

def extract_metadata_from_document(document):
    """Search metadata in a document

    Args:
       document: Document to be analyze.

    Raises:
        FileNotFoundError: If file doesn't exist.

    Returns:
        dict: A json with metadata
    """
    if isfile(document):
        return extract_metadata(document)
    raise FileNotFoundError()
