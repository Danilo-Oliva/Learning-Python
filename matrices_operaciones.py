import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Suma:\n", a + b)
print("Multiplicación elemento a elemento:\n", a * b)
print("Producto matricial:\n", a @ b)  # o np.dot(a, b)
print("Transpuesta:\n", a.T)
print("Inversa:\n", np.linalg.inv(a))   # inversa de la matriz
print("Determinante:", np.linalg.det(a))
