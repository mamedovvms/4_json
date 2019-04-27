import json
import os
import argparse


def load_data(filepath):
    with open(filepath) as file:
        try:
            return json.loads(file.read())
        except json.JSONDecodeError:
            return

def pretty_print_json(data_to_print):
    print(json.dumps(data_to_print, indent=4, ensure_ascii=False))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='File data in json format')
    params = parser.parse_args()
    filepath = params.filepath

    if not os.path.isfile(filepath):
        exit('Файл не найден')

    data_to_print = load_data(filepath)
    if not data_to_print:
        exit('Содержимое файла не в формате json')

    pretty_print_json(data_to_print)
