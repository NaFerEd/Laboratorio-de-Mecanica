from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

Periodos = np.array([2.04, 2.1, 2.27, 2.34, 2.42, 2.48, 2.53, 2.65, 2.7, 2.96])

Longitudes = np.array([1.0, 1.074, 1.2, 1.351, 1.4, 1.462, 1.582, 1.6, 1.8, 1.95]) 

slope, intercept, r_value, p_value, std_err = linregress(Periodos, Longitudes)

print(f"Ecuación de la recta: y = {slope:.4f}x + {intercept:.4f}")
print(f"Coeficiente de determinación R^2: {r_value**2:.4f}")

plt.scatter(Periodos, Longitudes, label="Datos Experimentales", color = "blue")
plt.xlabel("Longitudes (m)")
plt.ylabel("Periodo (s)")
plt.title("Grafica de los l - T")
plt.legend()
plt.grid(True)
plt.show()