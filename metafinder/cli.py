import argparse
from os import sep, listdir, remove
import os.path
from pathlib import Path

from metafinder.utils.banner import show_banner
from metafinder.core import processing


def main(argv=None):
    """The entry point for the script

   Args:
       argv (list): The list of parameters passed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--domain', help="Domain to search",required=True)
    parser.add_argument('-o','--output', help="Folder where the results will be stored",required=True, default="results")
    parser.add_argument('-l','--limit', help="Limit of documents to search", type=int, required=True)
    parser.add_argument('-t','--threads', help="Number of threads for downloading documents", type=int, default=4)
    parser.add_argument('-v','--verbose', help="Show results in terminal", action='store_true')
    args = parser.parse_args()
    show_banner()
    directory = Path(args.output) / args.domain
    directory.mkdir(parents=True, exist_ok=True)

    try:
        processing(args.domain, args.limit, args.verbose, str(directory), args.threads)
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

