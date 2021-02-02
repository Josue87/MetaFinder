from metafinder.utils.finder import google
from metafinder.utils.file.download import download_file
from metafinder.utils.file.parser import meta_parser, file_parser


def processing(target, limit, verbose, directory):
    links = google.search(target, limit)
    total_links = len(links)
    print(f"Total files to be analyzed: {total_links}")
    print("-------------------------------")
    if total_links > 0:
        metadata_files = download_file(links, target, directory)
        print("[+] Analyzing metadata...")
        if metadata_files:
            if verbose:
                meta_parser(metadata_files)
            file_parser(directory, "metadata_google.txt", metadata_files)
            print(f"[+] The results have been saved in the file {directory}/metadata_google.txt")
        else:
            print("[-] No metadata found...")
    else:
        print("[-] There is nothing to analyze. Closing...")

