import argparse
from os import sep, system
from utils.finder import google
from utils.directory.create import new_directory
from utils.file.download import download_file
from utils.file.parser import meta_parser, file_parser
from utils.banner import show_banner


def main(target, limit, verbose):
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
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', help="Target to search",required=True)
    parser.add_argument('-l','--limit', help="Limit of documents to search", type=int, required=True)
    parser.add_argument('-v','--verbose', help="Show results in terminal", action='store_true')
    args = parser.parse_args()
    show_banner()
    directory = "results" + sep + args.target
    new_directory(directory)
    try:
        main(args.target, args.limit, args.verbose)
    except KeyboardInterrupt:
        print("[-] MetaFinder has been interrupted. Deleting files.")
        system(f'rm {directory}/*')
        system('find . -name "*.tmp" -type f -delete')
        print("Bye.")
