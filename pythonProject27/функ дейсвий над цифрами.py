def calc (a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return ("Деление на ноль")
    else:
        return ("Операция не поддерживается")

print(calc(16,2, "+"))
print(calc(16,2,"-"))
print(calc(16, 2, "/"))
print(calc(16, 2, "*"))
print(calc(16, 0, "/"))



