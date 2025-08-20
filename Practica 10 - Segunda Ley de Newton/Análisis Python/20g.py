#-------------|
#Librerias    |
#-------------|

from math import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress



#--------------------------------------------------------------------------------------------

#Análisis del movimento

Tiempos = np.array([0.000, 0.042, 0.083, 0.125, 0.167, 0.208, 0.250, 0.292, 0.333, 0.375, 0.417, 0.458, 0.500, 0.542, 0.583, 0.625, 0.666, 0.708, 0.750, 0.791, 0.833, 0.875, 0.916, 0.958, 1.000, 1.041, 1.083, 1.125, 1.166, 1.208, 1.250, 1.291, 1.333, 1.375, 1.416, 1.458, 1.500, 1.541, 1.583, 1.625, 1.666])

Posiciones = np.array([0.000, 0.005, 0.011, 0.019, 0.026, 0.035, 0.046, 0.058, 0.071, 0.084, 0.097, 0.114, 0.129, 0.146, 0.167, 0.185, 0.205, 0.229, 0.249, 0.274, 0.300, 0.324, 0.349, 0.376, 0.406, 0.436, 0.466, 0.499, 0.533, 0.567, 0.601, 0.637, 0.673, 0.713, 0.751, 0.792, 0.833, 0.874, 0.923, 0.967, 1.006]) 

plt.scatter(Tiempos, Posiciones, label="Datos Experimentales", color = "Green")
plt.xlabel("Tiempos (s)")
plt.ylabel("Posición (m)")
plt.title("")
plt.legend()
plt.grid(True)
plt.show()

#Cambio de variable

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
tiempo (s) & $T = t^2$ ($s^2$) & posición (m) \\\\ \hline""")
for i in range(0, len(Tiempos)):
    print(f"{Tiempos[i] :.3f} (0.001) s & {TIEMPOS[i] :.3f} (0.001) $s^2$ & {Posiciones[i]:.3f} (0.001) m \\\\ \hline")
print("""
\\end{tabular}
\\caption{}
\\end{center}
\\end{table}""")

#----------------------------------------------------------------------
#Evalución de la fuerza
#----------------------------------------------------------------------
print("""
\\begin{table}[h!]
\\begin{center}
\\begin{tabular}{|c|c|}
\\hline
Cantidad & Valor \\\\ \hline""")

sum_t = sum(Tiempos)
print("$ \sum^{10}_{i = 1} t_i $ & " f"{sum_t :.3f} \\\\ \hline")

sum_t2 = sum(Tiempos**2)
print("$\sum^{10}_{i = 1} t_i^2$ & " f"{sum_t2 :.3f} \\\\ \hline")

sum_x = sum(Posiciones)
print("$\sum^{10}_{i = 1} x_i$ & " f"{sum_x :.3f} \\\\ \hline")

sum_tx = sum(Tiempos*Posiciones)
print("$\sum^{10}_{i = 1} tx_i$ & " f"{sum_tx :.3f} \\\\ \hline")

print(f"a & {slope :.4f} \\\\ \hline")

print(f"x_0 & {intercept :.3f} \\\\ \hline")

Sx = sqrt(sum((Posiciones-slope*Tiempos-intercept)**2)/(len(Tiempos)-2))

print(f"$S_x$ & {Sx :.3f} \\\\ \hline")

Sa = Sx*sqrt(len(Tiempos)/(len(Tiempos)*sum_t2 - sum_t**2))
print(f"$S_a$ & {Sa :.4f} \\\\ \hline")

print("""
\\end{tabular}
\\caption{}
\\end{center}
\\end{table}""")

M = 0.2122

m = 0.0200

mg = m*9.81

F = M*2*slope

SF = M*Sa

print(f"""
M = {M} (0.0001) kg \\\\

m = {m :.4} (0.0001) kg \\\\

mg = {mg :.3} (0.01) \\\\

a = {2*slope :.2} ({Sa :.1}) \\\\

F = ({2*slope :.2} """ "$\\frac{m}{s^2}$)" f"({M} kg) = {F :.2} ({SF :.1}) N \\\\""")

