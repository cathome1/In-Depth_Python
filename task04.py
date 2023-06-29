import decimal

user_balance = decimal.Decimal(0)
def add_money(balance):
    sum = int(input("Введите сумму пополнения кратную 50\n"))
    if(sum % 50 == 0):
        print("Средства зачислены на баланс пользователя")
        return balance + sum
def take_money(balance):
    sum = int(input(f"Введите сумму снятия кратную 50 и не больше {balance}\n"))
    procent = get_procent(sum)
    if sum % 50 == 0 and sum <= balance - procent:
        print("Средства сняты с баланса пользователя")
        return balance - procent - sum
    else:
        print("Невозможно снять средства, возможно вы не учли коммисию 1.5%")
        return balance
def get_procent(sum):
    if(sum <= 2000 ):
        return 30
    elif(sum >= 40000):
        return 600
    else:
        return (sum / 100) * 1.5

def menu_atm(balance):
    print("Здравствуйте, пользователь! Выберите действие")
    choise = input("\n1) Внести деньги\n2) Снять деньги\n3) Посмотреть баланс\n")
    match choise:
        case "1":
            return add_money(balance)
        case "2":
            return take_money(balance)
        case "3":
            print(f"Баланс на данный момент составляет: {balance}")
            return balance
        case _:
            print("Выбрано некоректное дейстивие! попробуйте снова.")
            return balance

count = 0
while True:
    if (user_balance >= 5000000):
        user_balance = user_balance - (user_balance / 10)
    if (count == 3):
        user_balance = user_balance + ((user_balance / 100) * 3)
        count = 0
    user_balance = menu_atm(user_balance)
    count += 1