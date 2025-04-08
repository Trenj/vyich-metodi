# -*- coding: utf-8 -*-

def forward_elimination(A, b):
    """Прямой ход метода Гаусса: приведение к треугольному виду"""
    n = len(A)
    for i in range(n):
        # Выбираем главный элемент (если нужно, можно добавить частичный выбор)
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    b[i], b[k] = b[k], b[i]
                    break
        
        # Делаем текущий элемент диагонали равным 1 и зануляем ниже
        diag = A[i][i]
        for j in range(i, n):
            A[i][j] /= diag
        b[i] /= diag

        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

def back_substitution(A, b):
    """Обратный ход метода Гаусса: нахождение решений"""
    n = len(A)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    return x

def gaussian_elimination(A, b):
    """Решение СЛАУ методом Гаусса"""
    forward_elimination(A, b)
    return back_substitution(A, b)

# Коэффициенты системы
A = [
    [20, 5, 7, 1],
    [-1, 13, 0, -7],
    [4, -6, 17, 5],
    [-9, 8, 4, -25]
]

# Правая часть
b = [-117, -1, 49, -21]

# Решение системы
solution = gaussian_elimination(A, b)

# Вывод результата
print("Решение системы:", solution)


"""
import numpy as np

# Коэффициенты системы
A = np.array([
    [20, 5, 7, 1],
    [-1, 13, 0, -7],
    [4, -6, 17, 5],
    [-9, 8, 4, -25]
])

# Вектор правой части
b = np.array([-117, -1, 49, -21])

# Решаем систему уравнений
x = np.linalg.solve(A, b)

# Выводим результат
print("Решение системы:", x)
"""
