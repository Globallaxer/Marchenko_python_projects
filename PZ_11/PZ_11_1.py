
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс  минимального элемента:
# Умножаем все элементы на минимальный элемент:
import random
vvod = int(input('Введите желаемое количество элементов - '))
sequence = [random.randint(-100, 100) for _ in range(vvod)]


with open('data_3.txt', 'w') as file:
    for num in sequence:
        file.write(str(num) + '\n')


with open('data_3.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]



min_value = min(numbers)
min_index = numbers.index(min_value)


multiplied_sequence = [num * min_value for num in numbers]


with open('data_4.txt', 'w') as file:
    file.write("Исходные данные:\n")
    file.write(str(numbers) + '\n\n')
    file.write("Количество элементов: " + str(len(numbers)) + '\n\n')
    file.write("Минимальный элемент: " + str(min_value) + '\n')
    file.write("Индекс минимального элемента: " + str(min_index) + '\n\n')
    file.write("Умножаем все элементы на минимальный элемент:\n")
    file.write(str(multiplied_sequence))


