# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
from pathlib import Path


def user_add(json_file: str) -> None:
    user_ids = set()
    all_dict = {}

    if Path(json_file).exists():
        with open(json_file, 'r', encoding='utf-8') as fr:
            all_dict = json.load(fr)
        for level, dict_ in all_dict.items():
            for id_, name in dict_.items():
                user_ids.add(id_)

    while True:
        name = input('Input user name: ')
        if name == ' ':
            break
        user_id = input('Input user ID: ')
        if user_id in user_ids:
            print('ID already exists')
            continue
        else:
            user_ids.add(user_id)
        access_level = int(input('Input access level: '))
        if access_level < 1 or access_level > 7:
            print('Access level must be 1 to 7')
            continue
        all_dict.setdefault(access_level, {})[user_id] = name

    with open(json_file, 'w', encoding='utf-8') as fw:
        json.dump(all_dict, fw, ensure_ascii=False, indent=2, sort_keys=True)


if __name__ == '__main__':
    user_add('users.json')

__all__ = ['user_add']
