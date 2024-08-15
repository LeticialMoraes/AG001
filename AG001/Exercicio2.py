import math

c = 352 % 10
# Definição da velocidade
def v(t, c):
    return 5 * c + 7 * t**4 + math.sqrt(t) - 3 * c * t**3

def integracao_numerica(f, a, b, n=1000):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

s_1 = integracao_numerica(lambda t: v(t, c), 0, 1)
s_7 = integracao_numerica(lambda t: v(t, c), 0, 7)

def aceleracao(v, t, c, delta=1e-5):
    return (v(t + delta, c) - v(t - delta, c)) / (2 * delta)

a_1 = aceleracao(v, 1, c)
a_7 = aceleracao(v, 7, c)

print("Deslocamento em t=1:", s_1)
print("Deslocamento em t=7:", s_7)
print("Aceleracao em t=1:", a_1)
print("Aceleracao em t=7:", a_7)
