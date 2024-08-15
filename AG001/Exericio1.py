import math

def func1(x):
    return (2 * x**2 - 7) / (7 * x**5 - 2)

# Aproximação para os limites
def numerical_limit(func, x_val, direction='both', delta=1e-9):
    if direction == 'both':
        return (func(x_val - delta) + func(x_val + delta)) / 2
    elif direction == 'left':
        return func(x_val - delta)
    elif direction == 'right':
        return func(x_val + delta)

c = 352 % 10  # Substitua 352 pelo seu número de matrícula
c1 = c + 1

lim1 = numerical_limit(lambda x: func1(x) * c1, -1)
lim2 = numerical_limit(lambda x: func1(x) * c1, 1e9)
lim3 = numerical_limit(lambda x: func1(x) * c1, -1e9)

print("Limite quando x -> -1:", lim1)
print("Limite quando x -> ∞:", lim2)
print("Limite quando x -> -∞:", lim3)
