from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

tiempos = np.array([0.0, 0.00012, 0.00024, 0.00036, 0.00048, 0.00060, 0.00072, 0.00084, 0.00096, 0.00108, 0.00120])

longitud = np.array([0.0, 0.0867, 0.1744, 0.2628, 0.3490, 0.4367, 0.5229, 0.6121, 0.6998, 0.7867, 0.8729])

slope, intercept, r_value, p_value, std_err = linregress(tiempos, longitud)

print(f"Ecuación de la recta: y = {slope:.4f}x + {intercept:.4f}")
print(f"Coeficiente de determinación R^2: {r_value**2:.4f}")

plt.scatter(tiempos, longitud, label="Datos Experimentales", color = "blue")
plt.plot(tiempos, slope * tiempos + intercept, label=f"Ajuste lineal: y = {slope:.4f}x + {intercept:.4f}", color = "red")
plt.xlabel("Tiempo (s)")
plt.ylabel("Longitud (m)")
plt.title("Regresión lineal - Tabla 4")
plt.legend()
plt.grid(True)
plt.show()


X = [0.0, 0.00012, 0.00024, 0.00036, 0.00048, 0.00060, 0.00072, 0.00084, 0.00096, 0.00108, 0.00120]

Y = [0.0, 0.0867, 0.1744, 0.2628, 0.3490, 0.4367, 0.5229, 0.6121, 0.6998, 0.7867, 0.8729]

EX, EY, EX2, EXY = 0, 0, 0, 0
N = len(X)

for x in X:
    EX = EX + x
    EX2 = EX2 + x**2

for y in Y:
    EY = EY + y

for n in range(N):
    EXY = EXY + X[n]*Y[n]
    

m = (N * EXY - EX * EY)/(N * EX2 - EX**2)

b = (EX2*EY - EX * EXY)/(N * EX2 - EX**2)

print(m, b)
    