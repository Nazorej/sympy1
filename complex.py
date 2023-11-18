import numpy as np
from sympy import symbols, Eq, solve

# Определяем символы
x, y = symbols('x y')

# Определяем уравнение кривой
curve_eq = Eq(x**3 + 1, y**2)

# Определяем диапазон значений x
x_values = np.linspace(-2, 3, 400)

# Вычисляем соответствующие значения y для каждого значения x
for x_value in x_values:
    solutions = solve(curve_eq.subs(x, x_value), y)
    for solution in solutions:
        if solution.is_real:
            print(f"Для x={x_value}, y={solution.evalf()} является действительным числом")
        else:
            print(f"Для x={x_value}, y={solution.evalf()} является комплексным числом")
