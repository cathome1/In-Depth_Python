# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
names = 1
games = True
far = "far"
supports = "test"

def s_delete():
    glob = globals()
    new_vars = {}
    for item in glob.keys():
        if item[-1] == "s":
            new_vars.update({f"{item[0:-1:1]}":glob[item]})
            glob[item] = None
    glob.update(new_vars)
    return True
print(globals())
s_delete()
print(globals())