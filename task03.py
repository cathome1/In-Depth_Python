# Пользователь вводит строку текста.
#  Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
#  Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
#  Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

text = input("Введите строку текста: ")
letters_dict = {}
count_letters = {}
for letter in text:
    try:
        letters_dict[letter] = letters_dict[letter] + 1
    except:
        letters_dict.update({letter: 1})
print(letters_dict)
for letter in text:
    count_letters.update({letter: text.count(letter)})
print(count_letters)
