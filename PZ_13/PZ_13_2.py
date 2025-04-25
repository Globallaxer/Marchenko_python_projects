# 2. В двумерном списке найти минимальный элемент в предпоследнем столбце.
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print(f"Исходная матрица: {matrix}")
min_mat = [row[-2] for row in matrix]
min_el = min(min_mat)
print(f'минимальный элемент в предпоследнем столбце: {min_el}')