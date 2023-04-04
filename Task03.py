# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import json
import csv


def json_to_csv(json_file_name: str) -> None:
    with open(json_file_name, 'r', encoding='utf-8') as json_f:
        json_dict = json.load(json_f)

    users_data = [[lvl, u_id, u_name]
                  for lvl, usr in json_dict.items()
                  for u_id, u_name in usr.items()]
    csv_file_name = f'{json_file_name.split(".")[0]}.csv'
    with open(csv_file_name, 'w', encoding='utf-8', newline='') as csv_f:
        csv_write = csv.writer(csv_f, dialect='excel')
        csv_write.writerows(users_data)


if __name__ == '__main__':
    json_to_csv('users.json')

__all__ = ['json_to_csv']
