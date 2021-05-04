import argparse
from os import sep, listdir, remove
import os.path
import sys
from pathlib import Path
from metafinder.utils.banner import show_banner
from metafinder.core import processing
from metafinder import __version__


def main(argv=None):
    """The entry point for the script

   Args:
       argv (list): The list of parameters passed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--domain', help="Domain to search",required=True)
    parser.add_argument('-o','--output', help="Folder where the results will be stored",required=True, default="results")
    parser.add_argument('-l','--limit', help="Limit of documents to search in the searchs engines (max 250)", type=int, required=True)
    parser.add_argument('-t','--threads', help="Number of threads for downloading documents", type=int, default=4)
    parser.add_argument('-go','--google', help="Search in Google", action='store_true', default=False)
    parser.add_argument('-bi','--bing', help="Search in Bing", action='store_true', default=False)
    parser.add_argument('-ba','--baidu', help="Search in Baidu", action='store_true', default=False)
    parser.add_argument('-v','--version', help="Show Metafinder version", action='version', version=__version__)

    args = parser.parse_args()
    show_banner()
    directory = Path(args.output) / args.domain
    directory.mkdir(parents=True, exist_ok=True)
    search_engines = {
        "google": args.google,
        "bing": args.bing,
        "baidu": args.baidu
    }
    some_election = False
    for k,v in search_engines.items():
        if v:
            some_election = True
            break
    
    if not some_election:
        search_engines["google"] = True

    limit = 250 if args.limit > 250 else args.limit # max 250

    try:
        processing(args.domain, limit, str(directory), args.threads, search_engines)
    except KeyboardInterrupt:
        print("[-] MetaFinder has been interrupted. Deleting files.")
        try:
            for f in listdir(directory):
                remove(os.path.join(directory, f))
        except:
            pass
        try:
            for f in listdir("."):
                if f.endswith(".tmp"):
                    remove(os.path.join(directory, f))
        except:
            pass
        print("Bye.")


if __name__ == '__main__':
    main(sys.argv[1:])

