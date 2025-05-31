def find_min_max(matrix):
    # "Разворачиваем" двумерный список в один плоский список с помощью sum и list comprehension
    flat_list = sum(matrix, [])
    
    # Находим минимальный и максимальный элементы
    min_element = min(flat_list)
    max_element = max(flat_list)
    
    return min_element, max_element

# Пример
Matr = [
    [3, 5, 1],
    [7, 2, 9],
    [4, 6, 8]
]

min_val, max_val = find_min_max(Matr)
print("Минимальный элемент:", min_val)
print("Максимальный элемент:", max_val)
