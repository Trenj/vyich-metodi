import math

# Функция, определяющая левую часть уравнения: f(x) = x - 2 + sin(1/x)
def f(x):
    return x - 2 + math.sin(1 / x)

# Производная функции f(x): f'(x) = 1 - cos(1/x) / x^2
def f_prime(x):
    return 1 - math.cos(1 / x) / (x ** 2)

# Метод Ньютона для приближённого нахождения корня уравнения
def newton_method(x0, epsilon, max_iterations=1000):
    iteration = 0  # Счётчик итераций

    # Повторяем, пока не достигнем нужной точности или не превысим число итераций
    while iteration < max_iterations:
        fx = f(x0)         # Вычисляем значение функции в текущей точке
        fpx = f_prime(x0)  # Вычисляем значение производной в текущей точке

        # Проверка на нулевую производную — метод Ньютона не может продолжать
        if fpx == 0:
            print("Производная равна нулю. Метод Ньютона не работает.")
            return None

        # Вычисляем новое приближение
        x1 = x0 - fx / fpx

        # Если разность между новым и предыдущим приближением меньше ε, решение найдено
        if abs(x1 - x0) < epsilon:
            return x1

        # Подготовка к следующей итерации
        x0 = x1
        iteration += 1

    # Если вышли из цикла — значит не достигли решения за max_iterations шагов
    print("Превышено максимальное число итераций")
    return None

# Исходные данные
a = 1.2            # Левая граница отрезка
b = 2.0            # Правая граница отрезка
epsilon = 0.0001   # Требуемая точность

# Начальное приближение — середина отрезка
x0 = (a + b) / 2

# Вызов метода Ньютона
root = newton_method(x0, epsilon)

# Вывод результата
if root is not None:
    print(f"Приближённый корень уравнения: {root}")
    print(f"Проверка: f({root}) = {f(root)}")
