from pathlib import Path
import tempfile
from os.path import isfile
from metafinder.utils.finder import google
from metafinder.utils.file.download import download_file
from metafinder.utils.file.metadata import extract_metadata


def extract_metadata_from_google_search(domain, limit=100, threads=4):
    """Search metadata in files through Google

    Args:
       domain: Target domain.
       limit: Maximum number of files to search.
       threads: Threads for downloading documents.
    
    Raises:
        GoogleCaptcha: If Google displays the captcha.
        Exception: If there is an error

    Returns:
        dict: A json with metadata
    """
    links = google.search(domain, limit)
    directory = tempfile.TemporaryDirectory()
    metadata_files = None
    if len(links) > 0:
        metadata_files = download_file(links, directory.name, threads, False)
    directory.cleanup()
    return metadata_files

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
