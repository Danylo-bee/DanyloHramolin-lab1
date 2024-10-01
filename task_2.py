from numpy import sin, inf, arange

# Параметри
a, b = 1.1, 2.0  # Інтервал табулювання
h = 0.1          # Крок табулювання
d = 0.001        # Допустима похибка

# Функція для обчислення значення ряду
def f_series(x, d):
    k = 1
    sum_value = 0
    term = inf
    while abs(term) > d:
        term = (1 / 2**k) * sin(x / 2**k)
        sum_value += term
        k += 1
    return sum_value    

# Табуляція
x_values = arange(a, b + h, h)
f_values = [f_series(x, d) for x in x_values]

# Виведення результатів у вигляді таблиці
for x, f_val in zip(x_values, f_values):
    print(f"x = {x:.2f}, f(x) = {f_val:.6f}")
