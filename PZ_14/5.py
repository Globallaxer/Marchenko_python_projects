def square_second_column(matrix):
    # Индекс второго столбца — 1 (нумерация с нуля)
    col_index = 1
    # Проходим по каждой строке и возводим элемент второго столбца в квадрат
    for row in matrix:
        if len(row) > col_index:
            row[col_index] = row[col_index] ** 2
    return matrix

# Пример
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_second_column(Matr)
for row in result:
    print(row)
