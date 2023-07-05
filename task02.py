# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировке Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text = input("Введите строку текста: ")
arr_text = text.split()
arr_text.sort(reverse=False)
max = 0
for item in arr_text:
    if len(item) > max:
        max = len(item)
for i in range(0, len(arr_text)):
    print(f"{i + 1} {arr_text[i]: >{max}}")
