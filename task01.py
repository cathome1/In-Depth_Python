# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
def _is_leap_year(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))


def is_true_date(str_date: str):
    list_date = str_date.split(".")
    if (len(list_date) != 3):
        return False
    list_date = list(map(int,list_date))
    date, month, year = list_date
    if(0>date>31 or 0>month>12 or 0>year>9999):
        return False
    if(month in (1,3,5,7,8,10,12) and date<=31):
        return True
    elif(month in (4,6,9,11) and date<=30):
        return True
    elif(month==2 and ((_is_leap_year(year) and date<=29) or (not _is_leap_year(year) and date<=28))):
            return True
    else:
        return False
