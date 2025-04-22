import math

# Дано
x_nodes = [0.2, 0.6, 1.0, 1.4]
x_star = 0.8

# Шаг 1: Вычисляем ω(x)
def omega(x, nodes):
    result = 1
    for xi in nodes:
        result *= (x - xi)
    return result

omega_x = omega(x_star, x_nodes)

# Шаг 2: Находим f⁽⁴⁾(x) = -6 / x^4 и его максимум на отрезке [0.2, 1.4]
def f4(x):
    return abs(-6 / (x ** 4))

# Ищем максимум на отрезке
a, b = min(x_nodes), max(x_nodes)
step = 0.0001
x = a
M4 = 0
while x <= b:
    val = f4(x)
    if val > M4:
        M4 = val
    x += step

# Шаг 3: Погрешность по формуле
n = len(x_nodes) - 1  # степень многочлена
factorial = math.factorial(n + 1)
error_estimate = (M4 * abs(omega_x)) / factorial

# Вывод результатов
print("Шаг 1: ω(x) =", omega_x)
print("Шаг 2: M₄ = max |f⁽⁴⁾(x)| на [0.2, 1.4] =", M4)
print("Шаг 3: Оценка погрешности |r₃(0.8)| <= ", error_estimate)
