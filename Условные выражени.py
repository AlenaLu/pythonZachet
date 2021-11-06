#Условные выражения

#Task #1.1
A = int(input())
cond_1 = A % 2 == 0
cond_2 = A % 3 == 0

if cond_1 or cond_2 is True:
    print("Число А кратно 2м или 3м")
else:
    print("Число А не кратно 2м или 3м")

#Task #1.11
A2 = int(input())
B2 = int(input())

cond_3 = A2 % 2 == 0
cond_4 = B2 % 2 == 0
if (cond_3 and not cond_4) or (cond_4 and not cond_3) is True:
    print("Только одно из чисел А или В чётное")
else:
    print("Либо оба числа А или В чётные или оба нечётные")

#Task #1.21
a = int(input())  # сторона треугольника а
b = int(input())  # сторона треугольника b
c = int(input())  # сторона треугольника c
# Условие проверки, что треугольник является прямоугольным
cond_var1 = c ** 2 == a ** 2 + b ** 2
cond_var2 = a ** 2 == c ** 2 + b ** 2
cond_var3 = b ** 2 == c ** 2 + a ** 2

if (cond_var1) or (cond_var2) or (cond_var3):
    print("треугольник с заданными сторонами а, b, c - является прямоугольным")
else:
    print("треугольник с заданными сторонами а, b, c - НЕ является прямоугольным")
