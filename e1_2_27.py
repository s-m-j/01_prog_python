"""
Равномерные случайные числа. Составьте программу, выводящую пять рав­
номерных случайных чисел типа f 1 оа t от О.О до 1.0, их среднее, минимальное
и максимальное значения. Используйте встроенные функции min ( ) и max( )
"""
import random

x1 = random.random()
x2 = random.random()
x3 = random.random()
x4 = random.random()
x5 = random.random()

print(x1,x2,x3,x4,x5,sep=',')
print((x1+ x2 + x3 + x4 + x5) / 5)
print(min(x1,x2,x3,x4,x5))
print(max(x1,x2,x3,x4,x5))

