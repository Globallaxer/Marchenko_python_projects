def double_column(matrix, N):
    # Проходим по каждой строке и, если в ней есть элемент с индексом N, умножаем его на 2
    for row in matrix:
        if len(row) > N:
            row[N] *= 2
    return matrix

# Пример матрицы
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ввод индекса столбца с клавиатуры
N = int(input(f"Введите индекс столбца N (от 0 до {len(Matr[0]) - 1}): "))

result = double_column(Matr, N)

print("Результат:")
for row in result:
    print(row)
