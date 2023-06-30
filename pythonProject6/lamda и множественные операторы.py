current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)