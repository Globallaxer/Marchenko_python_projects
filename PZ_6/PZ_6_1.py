# Дан список A размера N. Вывести вначале его элементы с нечетными номерами в
# порядке возрастания номеров, а затем — элементы с четными номерами в порядке
# убывания номеров: A1, A3, А5, …, A6, A4, A2. Условный оператор не использовать.
import random

while True:
    try:
        a = []
        n = int(input('Введите размер списка: '))
        i = 1
        while i <= n:
            b = random.randint(0,10)
            a.append(b)
            i += 1
        print(f'Список сгенерирован = {a}')    
        plus_numbers = a[0::2]
        minus_numbers = a[1::2][::-1]
        result = plus_numbers + minus_numbers
        print(f'Результат = {result}')   
        break

    except ValueError:
        print("Ошибка")       