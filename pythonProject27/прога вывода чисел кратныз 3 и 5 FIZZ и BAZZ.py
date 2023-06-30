def fizzbuzz(number):# -заводим функцию
  if number % 3 == 0 and number % 5 == 0:# указываем условие
    return "fizzbuzz" # -условие выполнения и её результат
  elif number % 3 == 0: # -новое условие
    return "fizz" # и новый результат э
  elif number % 5 == 0 : # eo` одно условие
    return "buzz" # ожидаемый результат от выполнения самой функции
  else :
    return number
for number in range(1,100):# прописф=ываем числа применения нашей функции.
  print(fizzbuzz(number)) # - выводим результат