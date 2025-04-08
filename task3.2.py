# -*- coding: utf-8 -*-
import math

# Функция, реализующая левую часть уравнения: f(x) = x - 2 + sin(1/x)
def f(x):
    return x - 2 + math.sin(1 / x)

# Производная функции f(x): f'(x) = 1 - cos(1/x) / x^2
def f_prime(x):
    return 1 - math.cos(1 / x) / (x ** 2)

# Метод Ньютона для численного решения уравнения
def newton_method(x0, epsilon, max_iterations=1000):
    iteration = 0  # Счетчик итераций

    # Проверяем, не превысили ли максимальное количество итераций или не достигли ли нужной точности
    while iteration < max_iterations:
        fx = f(x0)         # Вычисляем значение функции в текущей точке
        fpx = f_prime(x0)  # Вычисляем значение производной в текущей точке

        # Проверка на нулевую производную - в этом случае метод Ньютона не работает
        if fpx == 0:
            print("Производная = 0. Метод Ньютона не работает.")
            return None, iteration

        # Вычисляем следующее приближение
        x1 = x0 - fx / fpx

        # Если разница между приближениями меньше заданной точности, возвращаем результат
        if abs(x1 - x0) < epsilon:
            return x1, iteration + 1

        # Переходим к следующей итерации
        x0 = x1
        iteration += 1

    # Если мы вышли из цикла, значит превысили максимальное количество итераций
    print("Превышено максимальное количество итераций")
    return None, iteration

# Задаем параметры
a = 1.2            # Левая граница отрезка
b = 2.0            # Правая граница отрезка
epsilon = 0.0001   # Требуемая точность

# Выбираем начальное приближение - середина отрезка
x0 = (a + b) / 2

# Находим корень уравнения
root, iterations = newton_method(x0, epsilon)

# Выводим результат
if root is not None:
    print(f"Приближенный корень уравнения: {round(root, 3)}")
    print(f"Количество итераций: {iterations}")
    print(f"Проверка: f({round(root, 3)}) = {round(f(root), 3)}")