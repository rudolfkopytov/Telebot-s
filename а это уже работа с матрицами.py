test_matrix = [[1, 2, 3],
              [7, -1, 2],
              [123, 2, -1]]

max = test_matrix[0][0] # берем в качестве точки отсчета любой элемент из матрицы
for row in test_matrix:
   for el in row:
       # если элемент больше максимального, то это новый максимум
       if el > max:
           max = el
print(max)