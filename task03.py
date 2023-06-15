# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
from random import randint
num = randint(0, 1001)
def guess_number(number):
    print("Число от 0 до 1000 загадано")
    for i in range (1,11):
        a = int(input("Ваш вариант: "))
        if (a == number):
            print(f"Вы угадали число! Истрачено попыток: {i}")
            return i
        elif a > number:
            print(f"Загаданное число меньше числа {a}")
        elif a < number:
            print(f"Загаданное число больше числа {a}")
        print(f"Осталось {10 - i} попыток")
    print(f"Попытки кончились, загаданное число было {number}")

guess_number(num)