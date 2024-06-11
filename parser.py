import json

def parse_json(x):
    filename = str(x)
    path = filename.removesuffix('.json')
    filepath = str(path + '-parsed.json')
    getfile = open(filename)
    y = json.load(getfile)
    z = json.dumps(y, indent=2)
    f = open(filepath, 'w')
    f.write(z)
    getfile.close()

def get_list(path):
    with open(path, 'r') as file:
        files = file.read().splitlines()
    return files

def save_parses():
    x = get_list('./json-list.txt')

    for json_file in x:
        parse_json(json_file)

save_parses()
