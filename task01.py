# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json


def parse_info(file_name):
    try:
        with open(file_name, 'r+', encoding="utf-8") as f:
            dct = json.load(f)
    except:
        dct = {str(i): dict() for i in range(1, 8)}
    ids = []
    for i in dct.values():
        ids.extend(list(i.keys()))
    while True:
        args = input("Введите Имя, ID, Уровень Допуска через пробел в той же последовательности: ")
        if args == '':
            break
        user_name, user_id, user_access = args.split(' ')
        if user_id in ids:
            print("Пользователь с таким ID уже записан")
        elif 0 > int(user_access) or int(user_access) > 7:
            print("Такого уровня доступа не существует")
        else:
            dct[user_access][user_id] = user_name
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(dct, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    parse_info("file.json")
