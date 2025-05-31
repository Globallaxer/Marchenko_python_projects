def average_odd_rows(matrix):
    averages = {}
    for i in range(1, len(matrix), 2):
        row = matrix[i]
        if len(row) > 0:
            avg = sum(row) / len(row)
            averages[i] = avg
    return averages

# Пример
Matr = [
    [1, 2, 3],      
    [4, 5, 6],      
    [7, 8, 9],      
    [10, 11, 12]    
]

result = average_odd_rows(Matr)
for row_index, avg in result.items():
    print(f"Среднее арифметическое строки с индексом {row_index}: {avg}")
