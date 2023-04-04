# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import pickle
import csv


def pickle_to_csv(pickle_file_name: str, csv_file_name: str) -> None:
    with (
        open(pickle_file_name, 'rb') as pf,
        open(csv_file_name, 'w', encoding='utf-8', newline='') as csf
    ):
        data = pickle.load(pf)
        keys = []
        for key, val in data[0].items():
            keys.append(key)

        csv_file = csv.DictWriter(csf, fieldnames=keys, dialect='excel')
        csv_file.writeheader()
        csv_file.writerows(data)


if __name__ == '__main__':
    pickle_to_csv('new_users.pickle', 'new_table.csv')

__all__ = ['pickle_to_csv']
