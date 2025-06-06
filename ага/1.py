# def extract_inner_elements(Matr2):
#     # Определяем количество строк и столбцов
#     rows = len(Matr2)
#     cols = len(Matr2[0]) if rows > 0 else 0

#     # Используем list comprehension для выбора элементов,
#     # которые не находятся в первых и последних строках и столбцах
#     return [list(filter(lambda x: x is not None, row[1:-1])) for row in Matr2[1:-1]]

# Более функциональный вариант с map и filter:
def extract_inner_elements_func(Matr2):
    rows = len(Matr2)
    cols = len(Matr2[0]) if rows > 0 else 0

    # Отбираем "внутренние" строки (без первой и последней)
    inner_rows = list(filter(lambda r: True, Matr2[1:-1]))

    # Для каждой внутренней строки отбираем элементы без первого и последнего столбца
    return list(map(lambda row: list(map(lambda x: x, row[1:-1])), inner_rows))

# Пример использования:
Matr2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

Matr1 = extract_inner_elements_func(Matr2)
print(Matr1)
