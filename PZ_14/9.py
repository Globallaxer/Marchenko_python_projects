def replace_second_column(matrix, new_column):
    # Индекс второго столбца — 1
    col_index = 1
    # Проверяем, что длина new_column совпадает с числом строк матрицы
    if len(new_column) != len(matrix):
        raise ValueError("Размер одномерного массива не совпадает с числом строк матрицы")
    
    # Заменяем элементы второго столбца на элементы из new_column
    for i, row in enumerate(matrix):
        if len(row) > col_index:
            row[col_index] = new_column[i]
    return matrix

# Пример
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_col = [10, 20, 30]  # одномерный массив для замены второго столбца

result = replace_second_column(Matr, new_col)

for row in result:
    print(row)
