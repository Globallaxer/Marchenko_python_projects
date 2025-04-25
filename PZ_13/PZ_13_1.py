# Для каждого столбца матрицы с четным номером найти сумму ее элементов
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print(f"Исходная матрица: {matrix}")
total_sum = 0
for i in range(len(matrix[0])):
        if (i + 1) % 2 == 0: 
            col_sum = sum(row[i] for row in matrix)
            total_sum += col_sum
            print(f"Сумма в столбце {i + 1}: {col_sum}")


