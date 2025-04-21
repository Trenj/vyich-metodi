# -*- coding: utf-8 -*-

# Матрица коэффициентов системы
A = [
    [26, -9, -8, 8],
    [9, -21, -2, 8],
    [-3, 2, -18, 8],
    [1, -6, -1, 11]
]

# Вектор свободных членов
B = [20, -164, 140, -81]

# Преобразование системы к виду X = B*X + C
n = len(A)
B_matrix = [[0] * n for _ in range(n)]  # Матрица B
C_vector = [0] * n                      # Вектор C

for i in range(n):
    C_vector[i] = B[i] / A[i][i]  # Расчёт элемента вектора C
    for j in range(n):
        if i != j:
            B_matrix[i][j] = -A[i][j] / A[i][i]  # Расчёт элемента матрицы B

# Начальное приближение
X = [0] * n

# Погрешность и ограничение по числу итераций
epsilon = 0.001
max_iterations = 1000

# Метод простой итерации
def simple_iteration(B_matrix, C_vector, X, epsilon, max_iterations):
    n = len(B_matrix)
    
    for iteration in range(max_iterations):
        X_new = [0] * n
        
        for i in range(n):
            X_new[i] = sum(B_matrix[i][j] * X[j] for j in range(n)) + C_vector[i]
        
        # Проверка на сходимость
        diff = max(abs(X_new[i] - X[i]) for i in range(n))
        if diff < epsilon:
            return X_new, iteration + 1
        
        X = X_new  # Переход к следующей итерации
    
    raise ValueError("Метод не сошёлся за заданное число итераций")

# Решение системы
try:
    solution, iterations = simple_iteration(B_matrix, C_vector, X, epsilon, max_iterations)
    print(f"Solution: {solution}")
    print(f"Count of iterations: {iterations}")
except ValueError as e:
    print(e)
