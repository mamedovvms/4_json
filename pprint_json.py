import json
import sys
import os


def load_data(filepath):
    with open(filepath) as file:
        try:
            return json.loads(file.read())
        except json.JSONDecodeError:
            return

def pretty_print_json(data_for_print):
    print(json.dumps(data_for_print, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv[1]) == 0:
        print('Не введен путь к файлу')
        exit(0)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print('Файл не найден')
        exit(0)
    content_file_json = load_data(filepath)
    if not content_file_json:
        print('Содержимое файла не в формате json')
        exit(0)

    pretty_print_json(content_file_json)
