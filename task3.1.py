# -*- coding: utf-8 -*-
import math

# Функция, реализующая левую часть уравнения: f(x) = x - 2 + sin(1/x)
def f(x):
    return x - 2 + math.sin(1 / x)

# Преобразуем уравнение к виду x = g(x)
# x - 2 + sin(1/x) = 0 => x = 2 - sin(1/x)
def g(x):
    return 2 - math.sin(1 / x)

# Метод простой итерации
def simple_iteration(x0, epsilon, max_iterations=1000):
    iteration = 0
    
    while iteration < max_iterations:
        x1 = g(x0)  # Вычисляем новое приближение
        
        # Проверяем условие сходимости
        if abs(x1 - x0) < epsilon:
            return x1, iteration + 1
            
        x0 = x1  # Обновляем значение для следующей итерации
        iteration += 1
    
    raise ValueError("Метод не сошелся за указанное количество итераций")

# Задаем параметры
a = 1.2            # Левая граница отрезка
b = 2.0            # Правая граница отрезка
epsilon = 0.0001   # Требуемая точность
x0 = (a + b) / 2   # Начальное приближение

# Находим корень уравнения
try:
    root, iterations = simple_iteration(x0, epsilon)
    print(f"Приближенный корень уравнения: {round(root, 3)}")
    print(f"Количество итераций: {iterations}")
    print(f"Проверка: f({round(root, 3)}) = {round(f(root), 3)}")
except ValueError as e:
    print(e)
