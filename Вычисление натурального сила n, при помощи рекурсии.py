def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

sum_digit(123)  # 6