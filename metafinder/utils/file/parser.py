from os import sep
from metafinder.utils.var_data import *


def file_parser_list(directory, name, data):
    file_name = directory + sep + name
    with open(file_name, "w") as output:
        for d in data:
            output.write(f'{d}\n')

def file_parser(directory, name, metadata):
    file_name = directory + sep + name
    with open(file_name, "w") as output:
        for key, value in metadata.items():
            output.write("\n")
            output.write(key + "\n")
            output.write("-"* len(key) + "\n")
            output.write(f"URL: {value[CONST_URL]}\n")
            output.write(f"Status code: {value[CONST_STATUS_CODE]}\n")
            engines = ""
            for se in value[CONST_SEARCH_ENGINES]:
                engines = se + ", "
            output.write(f"Search engines: {engines[0:-2]}\n")
            if value[CONST_METADATA]:
                for v in value[CONST_METADATA]:
                    if value[CONST_METADATA][v] is not None:
                        output.write(f'|_ {v}: {value[CONST_METADATA][v]}\n')
            else:
                output.write(f'|_ No metadata found\n')

            