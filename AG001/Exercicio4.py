import math

def circuito(c):
    V1 = 7 + 5 * c
    V2 = 4 + 2 * c
    V3 = 3 + 4 * c

    R1 = 15000  # 15kΩ
    R2 = 10000  # 10kΩ
    R3 = 5000   # 5kΩ

    # Equações
    # V1 = I1 * R1 + (I1 - I2) * R2
    # V2 = I2 * R3
    # V3 = I2 * R2

    # Transformando as equações em um sistema linear
    A = [[R1 + R2, -R2],
         [-R2, R2 + R3]]

    B = [V1, V2]

    # Resolvendo o sistema de equações lineares
    det_A = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    I1 = (B[0] * A[1][1] - B[1] * A[0][1]) / det_A
    I2 = (A[0][0] * B[1] - A[1][0] * B[0]) / det_A

    return I1, I2

c = 352 % 10

I1, I2 = circuito(c)

print("Valores das correntes:")
print(f"I1 = {I1}")
print(f"I2 = {I2}")