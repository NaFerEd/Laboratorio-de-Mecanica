from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

tiempos = np.array([ 1.336, 1.670, 2.004, 2.338, 2.672, 3.006, 3.340, 3.674, 4.008, 4.342, 4.676, 5.010, 5.344, 5.678, 6.012, 6.346, 6.680, 7.014, 7.348, 7.682])

longitud = np.array([ 0.2098, 0.2572, 0.3042, 0.3524, 0.4003, 0.4508, 0.5022, 0.5513, 0.6005, 0.6466, 0.6957, 0.7445, 0.7910, 0.8384, 0.8818, 0.9256, 0.9757, 1.0195, 1.0630, 1.1095]) 

slope, intercept, r_value, p_value, std_err = linregress(tiempos, longitud)

print(f"Ecuación de la recta: y = {slope:.4f}x + {intercept:.4f}")
print(f"Coeficiente de determinación R^2: {r_value**2:.4f}")

plt.scatter(tiempos, longitud, label="Datos Experimentales", color = "green")
plt.plot(tiempos, slope * tiempos + intercept, label=f"Ajuste lineal: y = {slope:.4f}x + {intercept:.4f}", color = "#5e2129")
plt.xlabel("Tiempo (s)")
plt.ylabel("Longitud (m)")
plt.title("Regresión lineal - Tabla 3")
plt.legend()
plt.grid(True)
plt.show()