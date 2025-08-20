#-------------|
#Librerias    |
#-------------|

from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#--------------------------------------------------------------

#Análisis del movimento en el eje x

Tiempos = np.array([0.000, 0.033, 0.067, 0.100, 0.133, 0.167, 0.200, 0.233, 0.267, 0.300, 0.333, 0.367, 0.400, 0.433, 0.467, 0.500, 0.533, 0.567, 0.600, 0.633, 0.667, 0.700])

Posiciones = np.array([0.000, 0.085, 0.168, 0.250, 0.330, 0.410, 0.488, 0.567, 0.645, 0.719, 0.802, 0.878, 0.956, 1.030, 1.095, 1.167, 1.248, 1.326, 1.406, 1.488, 1.565, 1.655]) 

slope, intercept, r_value, p_value, std_err = linregress(Tiempos, Posiciones)

print(f"Ecuación de la recta: y = {slope:.3f}x + {intercept:.3f}")

plt.scatter(Tiempos, Posiciones, label="Datos Experimentales", color = "Green")
plt.plot(Tiempos, slope * Tiempos + intercept, label=f"Ajuste lineal: y = {slope:.4f}x + {intercept:.4f}", color = "black")
plt.xlabel("Tiempos (s)")
plt.ylabel("Posición (m)")
plt.title("")
plt.legend()
plt.grid(True)
plt.show()

print("""
\\begin{table}[h!]
\\begin{center}
\\begin{tabular}{|c|c|}
\\hline
tiempo (s) & posición (m) \\\\ \hline""")
for i in range(0, len(Tiempos)):
    print(f"{Tiempos[i] :.3f} (0.001) s & {Posiciones[i]:.3f} (0.001) m \\\\ \hline")
print("""
\\end{tabular}
\\caption{}
\\end{center}
\\end{table}""")

#--------------------------------------------------------------------------------------------
print("--------------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------------------

#Análisis del movimento en el eje y

Tiempos = np.array([0.000, 0.033, 0.067, 0.100, 0.133, 0.167, 0.200, 0.233, 0.267, 0.300, 0.333, 0.367, 0.400, 0.433, 0.467, 0.500, 0.533, 0.567, 0.600, 0.633, 0.667, 0.700])

Posiciones = np.array([0.000, 0.120, 0.226, 0.320, 0.396, 0.464, 0.517, 0.562, 0.597, 0.619, 0.631, 0.633, 0.621, 0.603, 0.574, 0.537, 0.484, 0.421, 0.343, 0.261, 0.161, 0.053]) 

plt.scatter(Tiempos, Posiciones, label="Datos Experimentales", color = "Green")
plt.xlabel("Tiempos (s)")
plt.ylabel("Posición (m)")
plt.title("")
plt.legend()
plt.grid(True)
plt.show()

#Cambio de variable para el eje y

TIEMPOS = Tiempos**2

slope, intercept, r_value, p_value, std_err = linregress(TIEMPOS, Posiciones)

print(f"Ecuación de la recta: y = {slope:.3f}x + {intercept:.3f}")

plt.scatter(TIEMPOS, Posiciones, label="Datos Experimentales", color = "Green")
plt.plot(TIEMPOS, slope * TIEMPOS + intercept, label=f"Ajuste lineal: y = {slope:.4f}x + {intercept:.4f}", color = "black")
plt.xlabel("Tiempos (s)")
plt.ylabel("Posición (m)")
plt.title("")
plt.legend()
plt.grid(True)
plt.show()  


print("""
\\begin{table}[h!]
\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
tiempo (s)$ $T = t^2$ ($s^2$) & posición (m) \\\\ \hline""")
for i in range(0, len(Tiempos)):
    print(f"{Tiempos[i] :.3f} (0.001) s & {TIEMPOS[i] :.3f} (0.001) s^2 & {Posiciones[i]:.3f} (0.001) m \\\\ \hline")
print("""
\\end{tabular}
\\caption{}
\\end{center}
\\end{table}""")

