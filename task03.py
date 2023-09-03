# Создайте функцию генератор чисел Фибоначчи
def fibonachi(count: int):
    start = 0
    next = 1
    yield start
    yield next
    for i in range(0, count + 1):
        new_start = next
        next = start + next
        start = new_start
        yield next


print(*fibonachi(4))
