import numpy as np

# Параметри
a, b = 1.1, 2.0  # Інтервал табулювання
h = 0.1          # Крок табулювання
d = 0.001        # Допустима похибка

# Функція для обчислення значення ряду
def f_series(x, tolerance):
    k = 1
    sum_value = 0
    term = np.inf
    while abs(term) > tolerance:
        term = (1 / 2**k) * np.sin(x / 2**k)
        sum_value += term
        k += 1
    return sum_value

# Табуляція
x_values = np.arange(a, b + h, h)
f_values = [f_series(x, d) for x in x_values]

# Виведення результатів у вигляді таблиці
for x, f_val in zip(x_values, f_values):
    print(f"x = {x:.2f}, f(x) = {f_val:.6f}")
