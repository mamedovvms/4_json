import json
import sys


def load_data(filepath):
    with open(filepath) as f:
        return json.loads(f.read())

def pretty_print_json(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    if len(sys.argv[1]) > 1:
        pretty_print_json(load_data(sys.argv[1]))