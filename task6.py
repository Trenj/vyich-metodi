def cubic_spline_variant5():
    # Входные данные варианта №5
    x = [0.2, 0.24, 0.27, 0.30, 0.32, 0.38]
    f = [1.2214, 1.2712, 1.3100, 1.3499, 1.3771, 1.4623]
    alpha = 21.5699  # M0 + M2
    beta = 3.3378    # M4 + M5
    x_eval = 0.25    # Точка для интерполяции

    n = len(x)
    h = [x[i+1] - x[i] for i in range(n-1)]

    # Сбор трёхдиагональной системы: A * c = b
    A = [[0.0]*n for _ in range(n)]
    b_vec = [0.0]*n

    # Граничное условие: c0 + c2 = alpha
    A[0][0] = 1
    A[0][2] = 1
    b_vec[0] = alpha

    # Внутренние уравнения
    for i in range(1, n-1):
        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]
        b_vec[i] = 6 * ((f[i+1] - f[i]) / h[i] - (f[i] - f[i-1]) / h[i-1])

    # Граничное условие: c4 + c5 = beta
    A[n-1][n-2] = 1
    A[n-1][n-1] = 1
    b_vec[n-1] = beta

    # Метод прогонки
    c = [0.0] * n
    alpha_tridiag = [0.0] * n
    beta_tridiag = [0.0] * n

    # Прямая прогонка
    alpha_tridiag[0] = -A[0][1] / A[0][0]
    beta_tridiag[0] = b_vec[0] / A[0][0]

    for i in range(1, n):
        denom = A[i][i] + A[i][i-1] * alpha_tridiag[i-1]
        alpha_tridiag[i] = -A[i][i+1] / denom if i < n-1 else 0
        beta_tridiag[i] = (b_vec[i] - A[i][i-1] * beta_tridiag[i-1]) / denom

    # Обратная прогонка
    c[n-1] = beta_tridiag[n-1]
    for i in range(n-2, -1, -1):
        c[i] = alpha_tridiag[i] * c[i+1] + beta_tridiag[i]

    # Вычисляем коэффициенты b и d
    b_coeffs = [0.0] * (n-1)
    d_coeffs = [0.0] * (n-1)

    for i in range(n-1):
        d_coeffs[i] = (c[i+1] - c[i]) / h[i]
        b_coeffs[i] = ((f[i+1] - f[i]) / h[i]) - h[i] * (2 * c[i] + c[i+1]) / 6

    # Поиск интервала, в который попадает x_eval
    for i in range(n-1):
        if x[i] <= x_eval <= x[i+1]:
            dx = x_eval - x[i]
            Sx = f[i] + b_coeffs[i]*dx + c[i]*dx**2/2 + d_coeffs[i]*dx**3/6
            break
    else:
        Sx = None  # x_eval вне диапазона

    # Вывод
    print("Значение S(0.25):", round(Sx, 6))
    print("Коэффициенты c:", [round(ci, 6) for ci in c])
    print("Коэффициенты b:", [round(bi, 6) for bi in b_coeffs])
    print("Коэффициенты d:", [round(di, 6) for di in d_coeffs])

# Запуск
cubic_spline_variant5()
