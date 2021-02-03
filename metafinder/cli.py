import argparse
from os import sep, system
from pathlib import Path

from metafinder.utils.banner import show_banner
from metafinder.core import processing


def main(argv=None):
    """The entry point for the script

   Args:
       argv (list): The list of parameters passed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', help="Target to search",required=True)
    parser.add_argument('-o','--output', help="Folder where the results will be stored",required=True, default="results")
    parser.add_argument('-l','--limit', help="Limit of documents to search", type=int, required=True)
    parser.add_argument('-v','--verbose', help="Show results in terminal", action='store_true')
    args = parser.parse_args()
    show_banner()
    directory = Path(args.output) / args.target
    directory.mkdir(parents=True, exist_ok=True)

    try:
        processing(args.target, args.limit, args.verbose, str(directory))
    except KeyboardInterrupt:
        print("[-] MetaFinder has been interrupted. Deleting files.")
        system(f'rm {directory}/*')
        system('find . -name "*.tmp" -type f -delete')
        print("Bye.")


if __name__ == '__main__':
    main(sys.argv[1:])

