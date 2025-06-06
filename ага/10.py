def replace_third_row(matrix, new_row):
    row_index = 2  # индекс третьей строки (нумерация с 0)
    if len(matrix) <= row_index:
        raise IndexError("В матрице нет третьей строки")
    if len(new_row) != len(matrix[row_index]):
        raise ValueError("Размер одномерного массива не совпадает с количеством столбцов в матрице")
    
    matrix[row_index] = new_row
    return matrix

# Пример
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

new_row = [100, 200, 300]  # одномерный массив для замены третьей строки

result = replace_third_row(Matr, new_row)

for row in result:
    print(row)
