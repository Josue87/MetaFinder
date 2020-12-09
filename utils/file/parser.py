from os import sep


def meta_parser(metadata):
    for key, value in metadata.items():
        print("\n")
        print(key)
        print("-"* len(key))
        for v in value:
            if value[v]:
                print(f'|_ {v}: {value[v]}')


def file_parser(directory, name, metadata):
    file_name = directory + sep + name
    with open(file_name, "w") as output:
        for key, value in metadata.items():
            output.write("\n")
            output.write(key + "\n")
            output.write("-"* len(key) + "\n")
            for v in value:
                if value[v]:
                    output.write(f'|_ {v}: {value[v]}\n')
            