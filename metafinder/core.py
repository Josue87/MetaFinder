from metafinder.utils.finder import google
from metafinder.utils.finder import bing
from metafinder.utils.finder import baidu
from metafinder.utils.file.download import download_file
from metafinder.utils.file.parser import meta_parser, file_parser
from metafinder.utils.color_print import print_error, print_ok


def processing(target, limit, verbose, directory, threads, search_engines):
    links = []
    search_engines_methods = {
        "google": google.search,
        "bing": bing.search,
        "baidu": baidu.search
     }
    for engine in search_engines_methods.keys():
        aux_links = []
        if search_engines.get(engine, False):
            print(f"Searching in {engine}")
            try:
                aux_links = search_engines_methods[engine](target, limit)
                for link in aux_links:
                    if link not in links:
                        links.append(link)
                print_ok("Done", end="\n")
            except KeyboardInterrupt:
                print(f"{engine} interrupted\n")
            except Exception as ex:
                 print_error(f"{engine} error {ex}", end="\n")
    total_links = len(links)
    print(f"Total files to be analyzed: {total_links}")
    print("-------------------------------")
    if total_links > 0:
        try:
            metadata_files = download_file(links, directory, threads)
            print("Analyzing metadata...")
            if metadata_files:
                if verbose:
                    meta_parser(metadata_files)
                filename = "metadata_result.txt"
                file_parser(directory, filename, metadata_files)
                print_ok(f"The results have been saved in the file {directory}/{filename}")
            else:
                print_error("No metadata found...")
        except KeyboardInterrupt:
            print("CTRL^C")
    else:
        print("There is nothing to analyze. Closing...")
