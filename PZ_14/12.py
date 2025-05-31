def sum_and_product_of_column(matrix, N):
    # Проверяем, что индекс столбца корректен для всех строк
    if not matrix or any(len(row) <= N for row in matrix):
        raise IndexError("Индекс столбца вне диапазона для одной или нескольких строк")

    total_sum = sum(row[N] for row in matrix)
    product = 1
    for row in matrix:
        product *= row[N]
    return total_sum, product

# Пример двумерного списка
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ввод индекса столбца с клавиатуры
N = int(input(f"Введите индекс столбца N (от 0 до {len(Matr[0]) - 1}): "))

try:
    s, p = sum_and_product_of_column(Matr, N)
    print(f"Сумма элементов столбца {N}: {s}")
    print(f"Произведение элементов столбца {N}: {p}")
except IndexError as e:
    print(e)
