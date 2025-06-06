def increase_row_by_3(matrix, N):
    if 0 <= N < len(matrix):
        # Увеличиваем каждый элемент строки N на 3
        matrix[N] = list(map(lambda x: x + 3, matrix[N]))
    else:
        print("Ошибка: индекс строки вне диапазона.")
    return matrix

# Пример матрицы
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ввод индекса строки с клавиатуры
N = int(input("Введите индекс строки N (от 0 до {}): ".format(len(Matr)-1)))

result = increase_row_by_3(Matr, N)

print("Результат:")
for row in result:
    print(row)
