x = 3


def func():
   global x # объявляем, что переменная является глобальной
   print(x)
   x = 5
   x += 5
   return x


func()
print(x)