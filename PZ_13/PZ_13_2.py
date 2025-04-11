matrix = [ 
      [1, 2, 3, 4],
     [ 5, 6, 7, 8]
     ]
min_mat = [row[-2] for row in matrix]
min_el = min(min_mat)
print(min_el)