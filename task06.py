# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
a = input("Введите первую дробь в формате a/b : ")
b = input("Введите вторую дробь в формате a/b : ")
a = a.split("/")
a[0],a[1] = int(a[0]),int(a[1])
b = b.split("/")
b[0],b[1] = int(b[0]),int(b[1])
sum = Fraction ((a[0] * b[1]) + (b[0] * a[1]),(a[1] * b[1]))
# sum = str((a[0] * b[1]) + (b[0] * a[1])) + '/' + str(a[1] * b[1]) # Если нельзя использовать Fraction для записи
print(sum)
test = Fraction(a[0],a[1]) + Fraction(b[0],b[1])
print(test)
