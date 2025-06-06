def cube_first_column(matrix):
    col_index = 0  # индекс первого столбца
    for row in matrix:
        if len(row) > col_index:
            row[col_index] = row[col_index] ** 3
    return matrix

# Пример
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = cube_first_column(Matr)
for row in result:
    print(row)
