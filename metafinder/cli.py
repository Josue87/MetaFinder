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
    parser.add_argument('-d', '--domain', help="Single domain to search")
    parser.add_argument('-df', '--domain-file', help="Path to the file containing domains (one per line)")
    parser.add_argument('-ds', '--domain-stdin', help="Read domains from stdin", action='store_true')
    parser.add_argument('-o', '--output', help="Folder where the results will be stored", required=True, default="results")
    parser.add_argument('-l', '--limit', help="Limit of documents to search in the search engines (max 250)", type=int, required=True)
    parser.add_argument('-t', '--threads', help="Number of threads for downloading documents", type=int, default=4)
    parser.add_argument('-go', '--google', help="Search in Google", action='store_true', default=False)
    parser.add_argument('-bi', '--bing', help="Search in Bing", action='store_true', default=False)
    parser.add_argument('-ba', '--baidu', help="Search in Baidu", action='store_true', default=False)
    parser.add_argument('-v', '--version', help="Show Metafinder version", action='version', version=__version__)

    args = parser.parse_args()
    show_banner()

    if args.domain and (args.domain_file or args.domain_stdin):
        print("Error: Please provide either a single domain (-d), a domain file (-df), or use stdin (-ds), not multiple options.")
        return
    elif args.domain_file and args.domain_stdin:
        print("Error: Please provide either a domain file (-df) or use stdin (-ds), not both.")
        return
    elif args.domain:
        domains = [args.domain]
    elif args.domain_file:
        try:
            with open(args.domain_file, 'r') as file:
                domains = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Error: File not found: {args.domain_file}")
            return
    elif args.domain_stdin:
        domains = [line.strip() for line in sys.stdin.readlines()]
    else:
        print("Error: Please provide either a single domain (-d), a domain file (-df), or use stdin (-ds).")
        return

    for domain in domains:
        print(f"\nProcessing domain: {domain}")
        directory = Path(args.output) / domain
        directory.mkdir(parents=True, exist_ok=True)
        search_engines = {
            "google": args.google,
            "bing": args.bing,
            "baidu": args.baidu
        }
        some_election = any(search_engines.values())
        
        if not some_election:
            search_engines["google"] = True

        limit = 250 if args.limit > 250 else args.limit  # max 250

        try:
            processing(domain, limit, str(directory), args.threads, search_engines)
            print(f"Processing for domain {domain} completed successfully.")
        except KeyboardInterrupt:
            print(f"[-] MetaFinder has been interrupted for domain: {domain}. Deleting files.")
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
            print(f"Processing for domain {domain} interrupted. Files deleted.")
            print("Bye.")

if __name__ == '__main__':
    main(sys.argv[1:])
