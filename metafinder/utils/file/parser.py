from os import sep


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
            output.write(f"URL: {value['url']}\n")
            for v in value["metadata"]:
                if value["metadata"][v] is not None:
                    output.write(f'|_ {v}: {value["metadata"][v]}\n')

            