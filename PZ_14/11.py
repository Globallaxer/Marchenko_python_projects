def sum_and_product_of_row(matrix, N):
    if 0 <= N < len(matrix):
        row = matrix[N]
        total_sum = sum(row)
        product = 1
        for val in row:
            product *= val
        return total_sum, product
    else:
        raise IndexError("Индекс строки вне диапазона")

# Пример двумерного списка
Matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ввод индекса строки с клавиатуры
N = int(input(f"Введите индекс строки N (от 0 до {len(Matr)-1}): "))

try:
    s, p = sum_and_product_of_row(Matr, N)
    print(f"Сумма элементов строки {N}: {s}")
    print(f"Произведение элементов строки {N}: {p}")
except IndexError as e:
    print(e)
