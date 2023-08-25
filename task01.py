# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
def index_sum(arr,ind1,ind2):
    if(ind1>=0 and ind1<len(arr) and ind2>=0 and ind2<len(arr)):
        sum = 0
        if ind1<ind2:
            for i in range(ind1,ind2+1):
                sum+=arr[i]
        elif ind1>ind2:
            for i in range(ind2,ind1+1):
                sum+=arr[i]
        return sum
    else:
        return None

print(index_sum([1,2,3,4,5,6,7,8,9,10],2,5))
