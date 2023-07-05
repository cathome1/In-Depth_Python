# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
friends = {
    "Дима": ("сигареты", "спички", "бумага", "вода"),
    "Андрей": ("палатка", "мангал", "вода"),
    "Илья": ("вода", "спички", "шашлык")
}
things = {}
count = 0
for friend_key in friends.keys():
    friend = friends[friend_key]
    for item in friend:
        try:
            things[item].append(friend_key)
        except:
            things.update({item:[friend_key]})
    if count == 0:
        all_friends = set(friend)
        unical = set(friend)
        not_unical = set()
    all_friends = all_friends & set(friend)
    if count > 0:
        not_unical = not_unical | (unical - (unical - set(friend)))
        unical = (unical - set(friend)) | (set(friend) - unical)
        unical = unical - not_unical
    count += 1
for thing in things.keys():
    outsider = set(friends.keys()) - set(things[thing])
    if (len(outsider) == 1):
        print(f"{str(outsider)} единственный кто не взял {thing}") # почему то множество не преобразуется в строку
print(f"Какие вещи взяли все три друга - {all_friends}")
print(f"Какие вещи уникальны, есть только у одного друга - {unical}")