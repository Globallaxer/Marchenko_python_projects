# Для каждого столбца матрицы с четным номером найти сумму ее элементов
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print(f"Исходная матрица: {matrix}")
total_sum = 0
column_sums = list(map(
    lambda col: sum(col),
    [column for i, column in enumerate(zip(*matrix)) if (i+1) % 2 == 0]
))

print(column_sums)


