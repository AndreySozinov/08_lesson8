# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде одноимённых pickle файлов.
from pathlib import Path
import json
import pickle


def json_to_pickle(dir_path: str) -> None:
    p = Path(Path(dir_path))
    for obj in p.iterdir():
        if obj.is_file() and obj.name.split('.')[-1] == 'json':
            with open(obj, 'r', encoding='utf-8') as f:
                json_file = json.load(f)

            csv_file_name = obj.name.replace('.json', '.pickle')
            with open(csv_file_name, 'wb') as f:
                pickle.dump(json_file, f)


if __name__ == '__main__':
    json_to_pickle(str(Path().cwd()))

__all__ = ['json_to_pickle']
