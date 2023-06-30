# Изограмма - это слово , в котором нет повторяющихся букв, последовательных или нет.Реализовать функцию. которая определяет, является ли строка, содержащая только буквы, изограммой. Предположим, что пустая строка является изограммой. Игнорировать регистр букв.
def is_isogram(string):
   string = string.lower()
   for letter in string:
     if string.count(letter) > 1: return False
   return True

print(is_isogram('aba'))