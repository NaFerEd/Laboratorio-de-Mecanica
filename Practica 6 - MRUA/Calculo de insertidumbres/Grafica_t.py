from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

Tiempos = np.array([0.7, 1.49, 2.0, 2.22, 2.58, 2.91, 3.13, 3.36, 3.44, 3.68])

distancias = np.array([5.2, 17.7, 30.2, 42.7, 55.2, 67.7, 80.2, 92.7, 105.2, 117.7]) 

plt.scatter(Tiempos, distancias, label="Datos Experimentales", color = "green")
plt.xlabel("Tiempo (s)")
plt.ylabel("Longitud (m)")
plt.title("Grafica de los t - s, de la Tabla 1")
plt.legend()
plt.grid(True)
plt.show()