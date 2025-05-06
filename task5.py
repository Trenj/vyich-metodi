# -*- coding: utf-8 -*-
import sys
import math

def f(x):
    return math.cos(x)

# Пределы интегрирования
a = math.pi / 4
b = 3 * math.pi / 4

# Точное значение интеграла
exact_value = math.sin(b) - math.sin(a)

# Шаг и число разбиений
h = 0.1
n = int((b - a) / h)

# Вычисление интеграла методом трапеций
integral = (f(a) + f(b)) * 0.5
for i in range(1, n):
    x_i = a + i * h
    integral += f(x_i)
integral *= h

# Оценка погрешности
max_f2 = 1  # max|f''(x)| = max|-cos(x)| ≤ 1
error_estimate = ((b - a) * h**2 / 12) * max_f2

# Вывод результатов
print(f"Приближённое значение интеграла: {integral:.6f}")
print(f"Точное значение интеграла: {exact_value:.6f}")
print(f"Разница с точным значением: {abs(integral - exact_value):.6f}")
print(f"Оценка погрешности (по формуле): {error_estimate:.6f}")

if error_estimate <= 0.01:
    print("Точность достигнута!")
else:
    print("Точность не достигнута, нужно уменьшить шаг h.")# -*- coding: utf-8 -*-
