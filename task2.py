import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 3 + 2 * x + 1

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість точок
N = 5000

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Максимум функції на [a, b]
f_max = max(f(np.linspace(a, b, 1000)))

# Генерація випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f_max, N)

# Які точки під кривою
under_curve = y_random <= f(x_random)

# Оцінка інтеграла
integral_estimate = (b - a) * f_max * np.sum(under_curve) / N
print(f"Оцінка інтеграла методом Монте-Карло: {integral_estimate}")

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Випадкові точки
ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=5, alpha=0.5, label='Точки під кривою')
ax.scatter(x_random[~under_curve], y_random[~under_curve], color='red', s=5, alpha=0.5, label='Точки над кривою')

# Межі інтегрування
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^3 + 2x + 1 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Перевірка

result, error = spi.quad(f, a, b)
print("Інтеграл: ", result, error)