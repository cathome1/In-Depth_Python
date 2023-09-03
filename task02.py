# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def gen_prize(name_list, tax_list, prize_procent_list):
    if len(name_list) == len(tax_list) == len(prize_procent_list):
        return {name_list[i]:(tax_list[i]/100*float(prize_procent_list[i][:-1])) for i in range(0,len(name_list)) }
    else: return -1

print(gen_prize(["Таня", "Вася", "Петя"],[100,300,500],["10%","15.3%","7.9%"]))