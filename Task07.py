# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.
import csv
import pickle


def csv_to_pickle_string(csv_file_name: str) -> None:
    with open(csv_file_name, 'r', newline='') as f:
        csv_file = csv.reader(f, dialect='excel')

        data = []
        for line in csv_file:
            data.append(line)

        result = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        print(result)


if __name__ == '__main__':
    csv_to_pickle_string('new_table.csv')

__all__ = ['csv_to_pickle_string']
