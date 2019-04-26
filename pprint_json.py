import json
import sys
import os


def load_data(filepath):
    with open(filepath) as file:
        try:
            return json.loads(file.read())
        except json.JSONDecodeError:
            return

def pretty_print_json(data_to_print):
    print(json.dumps(data_to_print, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if not len(sys.argv):
        exit('Не введен путь к файлу')

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        exit('Файл не найден')

    data_to_print = load_data(filepath)
    if not data_to_print:
        exit('Содержимое файла не в формате json')

    pretty_print_json(data_to_print)
