# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import json


def csv_to_json(source_file: str, goal_file: str) -> None:
    with (
        open(source_file, 'r', newline='') as f_csv,
        open(goal_file, 'w', encoding='utf-8') as f_json
    ):
        csv_file = csv.reader(f_csv)
        all_data = []
        for row in csv_file:
            user = {'level': row[0],
                    'ID': f'{row[1]:0>10}',
                    'name': row[2].capitalize(),
                    'hash': hash(f'{row[2]}{row[1]}')}
            all_data.append(user)
        json.dump(all_data, f_json, indent=2)


if __name__ == '__main__':
    csv_to_json('users.csv', 'new_users.json')

__all__ = ['csv_to_json']
