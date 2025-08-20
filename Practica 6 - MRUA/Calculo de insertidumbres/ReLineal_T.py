from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

Tiempos = np.array([0.49, 2.22, 4.0, 4.93, 6.66, 8.47, 9.8, 11.29, 11.83, 13.54])

distancias = np.array([5.2, 17.7, 30.2, 42.7, 55.2, 67.7, 80.2, 92.7, 105.2, 117.7]) 

slope, intercept, r_value, p_value, std_err = linregress(Tiempos, distancias)

print(f"Ecuación de la recta: y = {slope:.4f}x + {intercept:.4f}")
print(f"Coeficiente de determinación R^2: {r_value**2:.4f}")

plt.scatter(Tiempos, distancias, label="Datos Experimentales", color = "blue")
plt.plot(Tiempos, slope * Tiempos + intercept, label=f"Ajuste lineal: y = {slope:.4f}x  {intercept:.4f}", color = "red")
plt.xlabel("Tiempo (s)")
plt.ylabel("Longitud (m)")
plt.title("Regresión lineal de los T - s de la Tabla 1")
plt.legend()
plt.grid(True)
plt.show()