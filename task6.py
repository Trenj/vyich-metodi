import math

def cubic_spline_variant5():
    # === ЭТАП 1: Входные данные ===
    x = [0.2, 0.24, 0.27, 0.30, 0.32, 0.38]
    f = [1.2214, 1.2712, 1.3100, 1.3499, 1.3771, 1.4623]
    alpha = 21.5699
    beta = 3.3378
    x_eval = 0.25
    n = len(x)

    # === ЭТАП 2: Вычисление h_i ===
    h = [x[i+1] - x[i] for i in range(n-1)]

    # === ЭТАП 3: Формирование A * c = b ===
    A = [[0.0 for _ in range(n)] for _ in range(n)]
    b_vec = [0.0 for _ in range(n)]

    # Уравнение c0 + c2 = alpha
    A[0][0] = 1
    A[0][2] = 1
    b_vec[0] = alpha

    # Внутренние уравнения
    for i in range(1, n-1):
        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]
        df1 = (f[i+1] - f[i]) / h[i]
        df2 = (f[i] - f[i-1]) / h[i-1]
        b_vec[i] = 6 * (df1 - df2)

    # Уравнение c4 + c5 = beta
    A[n-1][n-2] = 1
    A[n-1][n-1] = 1
    b_vec[n-1] = beta

    # === ЭТАП 4: Решение методом прогонки ===
    # Прямой ход
    c = [0.0 for _ in range(n)]
    alpha_p = [0.0 for _ in range(n)]
    beta_p = [0.0 for _ in range(n)]

    alpha_p[0] = -A[0][1] / A[0][0] if A[0][0] != 0 else 0
    beta_p[0] = b_vec[0] / A[0][0] if A[0][0] != 0 else 0

    for i in range(1, n):
        a = A[i][i-1] if i >= 1 else 0
        b = A[i][i]
        c_ = A[i][i+1] if i < n-1 else 0
        denom = b + a * alpha_p[i-1]
        if denom == 0:
            raise ZeroDivisionError("Деление на ноль в прогонке")
        alpha_p[i] = -c_ / denom if i < n-1 else 0
        beta_p[i] = (b_vec[i] - a * beta_p[i-1]) / denom

    # Обратный ход
    c[n-1] = beta_p[n-1]
    for i in range(n-2, -1, -1):
        c[i] = alpha_p[i] * c[i+1] + beta_p[i]

    # === ЭТАП 5: Вычисление b_i и d_i ===
    b_coeffs = [0.0 for _ in range(n-1)]
    d_coeffs = [0.0 for _ in range(n-1)]

    for i in range(n-1):
        d_coeffs[i] = (c[i+1] - c[i]) / h[i]
        b_coeffs[i] = (f[i+1] - f[i]) / h[i] - h[i] * (2 * c[i] + c[i+1]) / 6

    # === ЭТАП 6: Определение нужного интервала для x_eval ===
    for i in range(n-1):
        if x[i] <= x_eval <= x[i+1]:
            segment = i
            break
    else:
        raise ValueError("x_eval вне диапазона")

    # === ЭТАП 7: Вычисление S(x_eval) ===
    dx = x_eval - x[segment]
    Sx = (
        f[segment]
        + b_coeffs[segment] * dx
        + c[segment] * dx**2 / 2
        + d_coeffs[segment] * dx**3 / 6
    )

    # === Вывод ===
    print(f"Значение S({x_eval}) ≈ {round(Sx, 6)}\n")
    print("Коэффициенты c:", [round(ci, 6) for ci in c])
    print("Коэффициенты b:", [round(bi, 6) for bi in b_coeffs])
    print("Коэффициенты d:", [round(di, 6) for di in d_coeffs])

# Запуск программы
cubic_spline_variant5()
