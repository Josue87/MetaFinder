from metafinder.utils.finder import google
from metafinder.utils.finder import bing
from metafinder.utils.finder import baidu
from metafinder.utils.file.download import download_file
from metafinder.utils.file.parser import file_parser_list, file_parser
from metafinder.utils.color_print import print_error, print_ok
from metafinder.utils.result import Result
from metafinder.utils.var_data import * 


def _get_links(target, limit, directory, threads, search_engines):
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
                for link_to_check in aux_links:
                    exist = False
                    i = 0
                    for exist_link in links:
                        if link_to_check == exist_link[CONST_URL]:
                            exist = True
                            links[i][CONST_SEARCH_ENGINES].append(engine)
                            break
                        i += 1

                    if not exist:
                        links.append({
                            CONST_SEARCH_ENGINES: [engine],
                            CONST_URL: link_to_check})
                print_ok("Done", end="\n")
            except KeyboardInterrupt:
                print(f"{engine} interrupted\n")
            except Exception as ex:
                 print_error(f"{engine} error {ex}", end="\n")
    return links


def processing(target, limit, directory, threads, search_engines):
    links = _get_links(target, limit, directory, threads, search_engines)
    total_links = len(links)
    links_msg = f"Total files to be analyzed: {total_links}"
    print(links_msg)
    print("-" * len(links_msg))
    if total_links > 0:
        try:
            metadata_result = Result(download_file(links, directory, threads))
            authors = metadata_result.get_authors()
            software = metadata_result.get_software()
            metadata_files = metadata_result.get_metadata()
            print("\nAnalyzing metadata...")
            if metadata_files:
                software_msg = f"Software data found: {len(software)}"
                authors_msg = f"Authors found: {len(authors)}"
                print(f"\n{authors_msg}")
                print("-" * len(authors_msg))
                for a in authors:
                    print(a)
                print(f"\n{software_msg}")
                print("-" * len(software_msg))
                for s in software:
                    print(s)
                metadata_filename = "metadata_result.txt"
                authors_filename = "authors.txt"
                software_filename = "software.txt"
                file_parser_list(directory, authors_filename, authors)
                file_parser_list(directory, software_filename, software)
                print("")
                print_ok(f"Authors data have been saved in file {directory}/{authors_filename}")
                print_ok(f"Software data have been saved in file {directory}/{software_filename}")
                file_parser(directory, metadata_filename, metadata_files)
                print_ok(f"All metadata results have been saved in file {directory}/{metadata_filename}")
            else:
                print_error("No metadata found...")
        except KeyboardInterrupt:
            print("CTRL^C")
        except:
            pass
    else:
        print("There is nothing to analyze. Closing...")
