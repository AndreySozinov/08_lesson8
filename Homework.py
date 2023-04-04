# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.
import os
import json
import csv
import pickle


def filescope(directory: str, result_filename: str) -> None:
    result_dict = []
    for dir_path, dir_name, file_name in os.walk(directory):
        if len(dir_name) != 0:
            for obj in dir_name:
                obj_dict = {'name': obj,
                            'parent_name': dir_path.split('\\')[-1],
                            'type': 'dir',
                            'size': _get_dir_size(os.path.join(dir_path, obj))}
                result_dict.append(obj_dict)
        if len(file_name) != 0:
            for obj in file_name:
                obj_dict = {'name': obj,
                            'parent_name': dir_path.split('\\')[-1],
                            'type': 'file',
                            'size': os.path.getsize(os.path.join(dir_path, obj))}
                result_dict.append(obj_dict)
    _save_to_json(result_dict, result_filename)
    _save_to_csv(result_dict, result_filename)
    _save_to_pickle(result_dict, result_filename)


def _get_dir_size(dir_path: str) -> int:
    total_size = 0
    for dirpath, _, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Пропускаем символьные ссылки
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def _save_to_json(data: list, filename: str) -> None:
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def _save_to_csv(data: list, filename: str) -> None:
    with open(f'{filename}.csv', 'w', encoding='utf-8', newline='') as f:
        csv_file = csv.DictWriter(f, fieldnames=['name', 'parent_name', 'type', 'size'], dialect='excel')
        csv_file.writeheader()
        csv_file.writerows(data)


def _save_to_pickle(data: list, filename: str) -> None:
    with open(f'{filename}.pickle', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    filescope(os.getcwd(), 'result')

__all__ = ['filescope']
