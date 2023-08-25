# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def arguments(**kwargs):
    new_dict = {}
    for item in vars()["kwargs"].items():
        try:
            hash(item[1])
            new_dict.update({item[1]: item[0]})
        except:
            new_dict.update({str(item[1]): item[0]})
    return new_dict


print(arguments(a=[1, 2], b=7))
