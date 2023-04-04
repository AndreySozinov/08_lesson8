# Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.
import json


def file_to_json(source_file: str, result_file: str) -> None:
    with(
        open(source_file, 'r', encoding='utf-8') as file1,
        open(result_file, 'w', encoding='utf-8') as result
    ):
        my_dict = {}
        for line in file1:
            key, value = line.split()
            key = str(key).capitalize()
            value = float(value[:-1])
            my_dict[key] = value
        json.dump(my_dict, result, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    file_to_json('Source_for_task1.txt', 'output.json')

__all__ = ['file_to_json']
