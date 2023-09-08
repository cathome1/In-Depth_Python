# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# 1,5 2,1 3,8 4,6 5,3 6,7 7,2 8,4

# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок

from random import randint

false_variants = set()
true_variants = set()

def _queen_power(x, y):
    queen_moves = []
    for i in range(1, 9):
        queen_moves.extend([(str(x), str(i)), (str(i), str(y))])
    new_x, new_y = int(x), int(y)
    while (new_x <= 8 and new_y <= 8):
        new_x += 1
        new_y += 1
        if (new_x < 9 and new_y < 9): queen_moves.append((str(new_x), str(new_y)))
    new_x, new_y = int(x), int(y)
    while (new_x >= 1 and new_y >= 1):
        new_x -= 1
        new_y -= 1
        if (new_x > 0 and new_y > 0): queen_moves.append((str(new_x), str(new_y)))
    new_x, new_y = int(x), int(y)
    while (new_x <= 8 and new_y >= 1):
        new_x += 1
        new_y -= 1
        if (new_x < 9 and new_y > 0): queen_moves.append((str(new_x), str(new_y)))
    new_x, new_y = int(x), int(y)
    while (new_x >= 1 and new_y <= 8):
        new_x -= 1
        new_y += 1
        if (new_x > 0 and new_y < 9): queen_moves.append((str(new_x), str(new_y)))
    return queen_moves


def check_safety_of_queens(queen_list):
    targets = queen_list.copy()
    for queen in queen_list:
        targets.remove(queen)
        attack = _queen_power(queen[0], queen[1])
        for target in targets:
            if target in attack:
                return False
    return True


def random_queens(quantity):
    list_queens = set()
    while len(list_queens) < quantity:
        list_queens.add((str(randint(1, 8)), str(randint(1, 8))))
    return list_queens

def check_false_variants(queens):
    global false_variants
    if queens in false_variants:
        return False
    return True

def check_true_variants(queens):
    global true_variants
    if queens in true_variants:
        return False
    return True

def check_all_variants(need_vars):
    count = 0
    while len(true_variants) < need_vars:
        queens = frozenset(random_queens(8))
        if check_true_variants(queens) and check_false_variants(queens):
            if check_safety_of_queens(list(queens)):
                true_variants.add(frozenset(queens))
                print(queens)
            else:
                false_variants.add(frozenset(queens))
                count += 1
                print(count)
    return true_variants


if __name__ == '__main__':
    # queens = input("Введите 8 координат ферзей в формате: x1,y1 x2,y2 ... x7,y7 x8,y8\n")
    # list_queens = list(map(tuple, queens.replace(",", "").split(" ")))
    # print(check_safety_of_queens(list_queens))
    print(*check_all_variants(4), sep="\n")
