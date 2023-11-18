import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve

# Определяем символы
x, y = symbols('x y')

# Определяем уравнение кривой
curve_eq = Eq(x**3 + 1, y**2)

# Определяем диапазон значений x
x_values = np.linspace(-4, 4, 800)

# Создаем массивы для значений y такого же размера, как x_values, и заполняем их nan
y_values_pos = np.full_like(x_values, np.nan)
y_values_neg = np.full_like(x_values, np.nan)

# Вычисляем соответствующие значения y для графика
for i, x_value in enumerate(x_values):
    solutions = solve(curve_eq.subs(x, x_value), y)
    if solutions[0].is_real:
        y_values_neg[i] = solutions[0].evalf()
    if solutions[1].is_real:
        y_values_pos[i] = solutions[1].evalf()

# Строим график для положительных значений y
plt.plot(x_values, y_values_pos, label='y²=x³+1')

# Строим график для отрицательных значений y
plt.plot(x_values, y_values_neg, label='y²=x³+1')

# Добавляем оси x и y
plt.axhline(0, color='black')  # ось y
plt.axvline(0, color='black')  # ось x

# Добавляем деления на ось y
plt.yticks(np.arange(-4, 5, 1))

# Добавляем деления на ось x
plt.xticks(np.arange(-4, 5, 1))

# Добавляем легенду
plt.legend()

# Получаем текущие оси
ax = plt.gca()

# Перемещаем ось y в центр
ax.spines['left'].set_position('center')

# Устанавливаем одинаковый масштаб для осей x и y
plt.axis('equal')

# Добавляем подписи к осям
plt.xlabel('x')
ax.set_ylabel('y', rotation=0, labelpad=10)
ax.yaxis.set_label_coords(-0.1, 0.5)

# Решаем уравнение для каждого значения x и выводим только целые решения
for x_value in range(-10, 11):
    solutions = solve(curve_eq.subs(x, x_value), y)
    real_solutions = [sol.evalf() for sol in solutions if sol.is_real and sol.is_integer]
    if real_solutions:
        for y_value in real_solutions:
            plt.plot(x_value, y_value, 'ro')  # 'ro' означает красные круглые маркеры
            plt.hlines(y_value, 0, x_value, colors='red', linestyles='dashed')  # пунктирная линия от точки до оси y
            plt.vlines(x_value, 0, y_value, colors='red', linestyles='dashed')  # пунктирная линия от точки до оси x
            print(f"Найдена точка (x={x_value}, y={int(y_value)})")

# Показываем график
plt.show()
