from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

Tiempos = np.array([2.04, 2.1, 2.27, 2.34, 2.42, 2.48, 2.53, 2.65, 2.7, 2.96])

distancias = np.array([1.0, 1.036, 1.095, 1.162, 1.183, 1.209, 1.258, 1.265, 1.342, 1.396]) 

slope, intercept, r_value, p_value, std_err = linregress(distancias, Tiempos)

print(f"Ecuación de la recta: y = {slope:.4f}x + {intercept:.4f}")
print(f"Coeficiente de determinación R^2: {r_value**2:.4f}")

plt.scatter(distancias, Tiempos, label="Datos Experimentales", color = "blue")
plt.plot(distancias, slope * distancias + intercept, label=f"Ajuste lineal: y = {slope:.4f}x  {intercept:.4f}", color = "red")
plt.xlabel("Longitudes (m)")
plt.ylabel("Promedios (s)")
plt.title("Regresión lineal de las L - T")
plt.legend()
plt.grid(True)
plt.show()