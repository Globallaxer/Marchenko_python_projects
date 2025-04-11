# Для каждого столбца матрицы с четным номером найти сумму ее элементов
matrix = [ 
      [1, 2, 3, 4],
     [ 5, 6, 7, 8]
     ]
total_sum = 0
for i in range(len(matrix[0])):
        if (i + 1) % 2 == 0: 
            col_sum = sum(row[i] for row in matrix)
            total_sum += col_sum
            print(f"Сумма в столбце {i + 1}: {col_sum}")


