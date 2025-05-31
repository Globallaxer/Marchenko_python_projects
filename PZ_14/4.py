def double_non_diagonal(matrix):
    n = len(matrix)
    # Создаем новый список, где элементы на главной диагонали остаются без изменений,
    # а остальные умножаются на 2
    return [
        list(map(lambda x_j: x_j[1] * 2 if x_j[0] != i else x_j[1], enumerate(row)))
        for i, row in enumerate(matrix)
    ]

# Пример
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = double_non_diagonal(Matr)
for row in result:
    print(row)
