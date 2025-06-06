def double_main_diagonal(matrix):
    n = len(matrix)
    # Предполагается, что матрица квадратная или хотя бы количество строк равно количеству столбцов
    for i in range(n):
        matrix[i][i] *= 2
    return matrix

# Пример
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = double_main_diagonal(Matr)
for row in result:
    print(row)
