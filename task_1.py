import math

# Визначаємо функцію для обчислення
def calculate_function(x):
    if x < 0.2:
        return math.log(3 * x + 1, 5)
    elif 0.2 <= x < 0.4:
        return x ** math.cos(x)
    elif x >= 0.4:
        return 1 / math.sin(math.log(x))

# Основні параметри
a = 0.1  # початок проміжку
b = 0.7  # кінець проміжку
h = 0.05 # крок табуляції

# Табулювання функції
for x in range(int(a * 100), int((b + h) * 100), int(h * 100)):
    x /= 100  # Перетворюємо значення назад в нормальний формат
    result = calculate_function(x)
    print(f"x = {x:.2f}, f(x) = {result:.5f}")