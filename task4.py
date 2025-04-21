# -*- coding: utf-8 -*-
import math

# Заданные точки
x_values = [0.2, 0.6, 1.0, 1.4]
y_values = [math.log(x) for x in x_values]

# Точка, в которой нужно вычислить значение
x_star = 0.8

# Функция интерполяции Лагранжа
def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
        
    return result

# Вычисление интерполяционного значения
P_x = lagrange_interpolation(x_values, y_values, x_star)

# Точное значение
true_value = math.log(x_star)

# Погрешность
error = abs(P_x - true_value)

# Вывод результатов
print(f"Интерполяционное значение в x* = {x_star}: {P_x}")
print(f"Точное значение ln({x_star}) = {true_value}")
print(f"Абсолютная погрешность: {error}")
